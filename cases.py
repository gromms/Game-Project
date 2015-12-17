

class Case_Handler():
	def __init__(self, case):
		self.case = case

	def updateDict(self, case, obj):
		newCase = {}
        for i in self.case:
            if i != self.obj:
                newCase[i] = False
            else:
                newCase[i] = True
        return newCase