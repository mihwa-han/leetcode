class Solution:
    def compareVersion(self, version1, version2):
        v1=version1.split('.')
        v2=version2.split('.')

        n = min(len(v1),len(v2))
        m = max(len(v1),len(v2))

        for i in range(n):
            if int(v1[i]) > int(v2[i]):
                return 1
            if int(v1[i]) < int(v2[i]):
                return -1

        if n==m:
            return 0

        if (len(v1)==n) & any(int(k) != 0 for k in v2[n:]):
            return -1

        if (len(v2)==n) & any(int(k) != 0 for k in v1[n:]):
            return 1

        return 0
