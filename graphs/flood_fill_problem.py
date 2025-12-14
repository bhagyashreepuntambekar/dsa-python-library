class Solution:
    def flood_fill(self,img,sr,sc,newColor):
      new_img = self._dfs(img,sr,sc,newColor,img[sr][sc])
      return new_img

    def _dfs(self,img,sr,sc,newColor,oldColor):
        m = len(img)
        n = len(img[0])

        if sr < 0 or sc<0 or sr>=m or sc>=n or img[sr][sc] != oldColor or img[sr][sc] ==newColor:
            return

        img[sr][sc] = newColor

        self._dfs(img, sr+1, sc, newColor, oldColor)
        self._dfs(img, sr-1, sc, newColor, oldColor)
        self._dfs(img, sr, sc+1, newColor, oldColor)
        self._dfs(img, sr, sc-1, newColor, oldColor)

        return img
def main():
    sol = Solution()
    image = [
        [1, 1, 1],
        [1, 1, 0],
        [1, 0, 1]
    ]
    sr = 1
    sc = 1
    newColor = 2
    print(sol.flood_fill(image,sr,sc,newColor))



if __name__ =="__main__":
    main()



