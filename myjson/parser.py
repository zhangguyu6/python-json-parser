from .tokens import WrongGrammarError


class Parse:
    def __init__(self, tokens):
        self.tokens = tokens
        self.index = 0

    def step(self):
        """
        进位并返回当前token
        """
        self.index += 1
        if self.index < len(self.tokens):
            return self.tokens[self.index]
        return None

    def peek(self):
        """
        查看当前值,不进位
        """
        if self.index < len(self.tokens):
            return self.tokens[self.index]
        return None

    def parse_value(self):
        """
        调用前当前 token 应当是 'BEGIN_OBJECT','BEGIN_ARRAY' 或者终点元素
        调用后当前 token 应当是 'END_OBJECT','END_ARRAY' 或者终点元素
        """
        token = self.peek()

        # 每个 value 的解析完毕后应当确保没有分界符
        if token[0] == 'BEGIN_OBJECT':
            return self.parse_object()

        elif token[0] == 'BEGIN_ARRAY':
            return self.parse_array()

        elif token[0] == 'STRING':
            return token[1]

        elif token[0] == 'BOOlEAN':
            return token[1]

        elif token[0] == 'NULL':
            return token[1]

        elif token[0] == 'INT':
            return token[1]

        elif token[0] == 'FLOAT':
            return token[1]

        else:
            raise WrongGrammarError(
                "token {} at {} is not a value".format(token, self.index))

    def parse_object(self):
        """
        调用前当前 token 应当是 'BEGIN_OBJECT'
        调用后当前 token 应当是 'END_OBJECT'
        """

        current_obj = {}
        # 'BEGIN_OBJECT' 的 下一位,应当是 'STRING' 或者 'END_OBJECT'
        token = self.step()
        while token[0] != 'END_OBJECT':
            if token[0] == 'STRING':
                key = token[1]
                token = self.step()
                if token[0] != 'COLON':
                    raise WrongGrammarError
                else:
                    # 此时当前 token 应为一个value
                    token = self.step()
                    value = self.parse_value()
                    current_obj[key] = value
                    # 此时当前 token 应为 'COLON' 或者 'END_OBJECT'
                    token = self.step()

            elif token[0] == 'COMMA':
                token = self.step()
            else:
                raise WrongGrammarError(
                    "token {} at {} can not convert object".format(token, self.index))
        return current_obj

    def parse_array(self):
        """
        调用前当前 token 应当是 'BEGIN_ARRAY'
        调用后当前 token 应当是 'END_ARRAY'
        """
        current_array = []
        # 'BEGIN_ARRAY' 的下一位,应当是 value 或者 'END_ARRAY'
        token = self.step()
        while token[0] != 'END_ARRAY':
            value = self.parse_value()
            current_array.append(value)
            token = self.step()
            if token[0] == 'COMMA':
                self.step()
        return current_array
