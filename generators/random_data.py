import random
import string


class RandomData:

    def random_string(self, prefix, maxlen):
        symbols = string.ascii_letters + string.digits + " "*3
        return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])