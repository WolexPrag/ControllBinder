class WindowOrder:
    Cells = [[4, 9, 7, 7, 8, 4, 8, 8, 9],[5,8,4,3,7,10,2]]
    def GetCurrentOrder(self,index:int,currentPage:int):
        return 2
    def GetCountPage(self):
        return 2
    def SetAllOrders(self):
        pageCurrent:int = 0
        while(pageCurrent<self.GetCountPage()):
            self.SetOrderForPage(pageCurrent)
            pageCurrent += 1
        pass
    def SetOrderForPage(self,page:int):
        pass