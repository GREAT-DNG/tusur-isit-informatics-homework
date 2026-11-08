class HashMap:
    def __init__(self, size=10):
        self.size = size
        self.buckets = [[] for _ in range(size)]
        self.count = 0

    def bucket(self, key):
        return self.buckets[hash(key) % self.size]

    def put(self, key, value):
        bucket = self.bucket(key)
        for i, (k, _) in enumerate(bucket):
            if k == key:
                bucket[i] = (k, value)
                return
        bucket.append((key, value))
        self.count += 1

    def get(self, key):
        for k, value in self.bucket(key):
            if k == key: return value
        raise KeyError(key)

    def remove(self, key):
        bucket = self.bucket(key)
        for i, (k, _) in enumerate(bucket):
            if k == key:
                del bucket[i]
                self.count -= 1
                return
        raise KeyError(key)

    def contains(self, key):
        for k, _ in self.bucket(key):
            if k == key: return True
        return False

    def __len__(self):
        return self.count
