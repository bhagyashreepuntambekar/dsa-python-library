class HashTable:

    def __init__(self,capacity = 10):
        self.capacity =  capacity
        self.size = 0
        self.buckets = [[] for _ in range(capacity)]

    def _hash(self,key):

        return hash(key) % self.capacity

    def put(self,key,value):

        index = self._hash(key)
        bucket = self.buckets[index]

        for i,(k,v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key,value)
                return
        bucket.append((key,value))
        self.size +=1

        if self.size / self.capacity > 0.7:
            self._resize()

    def get(self,key):

        index = self._hash(key)
        bucket = self.buckets[index]

        for k,v in bucket:
            if k == key:
                return v
        return None

    def remove(self,key):

        index = self._hash(key)
        bucket = self.buckets[index]

        for i,(k,v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                self.size -= 1
                return True
        return False

    def _resize(self):
        old_bucket = self.buckets
        self.capacity *= 2
        self.buckets = [[] for _ in range(self.capacity)]
        self.size = 0

        for bucket in old_bucket:
            for k,v in bucket:
                self.put(k,v)

    def __len__(self):
        return self.size

    def __str__(self):
        pairs = [f"{k}:{v}" for bucket in self.buckets for k,v in bucket]

        return "{" + ",".join(pairs) + "}"