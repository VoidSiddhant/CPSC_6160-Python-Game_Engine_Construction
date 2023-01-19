class isInside:
    def __init__(self, name = "action if is inside rect"):
        self.types = ["loop"]
        self.entity = None
        self.name = name
        self.verbose = False
        self.children = []
        return

    def shouldAct(self,data):
        if self.entity == None:
            return False
        if self.entity.active == False:
            return False


        return False

    def act(self, data):
        if self.shouldAct(data):

            for c in self.children:
                c.act(data)

            if self.verbose:
                print(self.name +"triggered for "+ self.entity.name)
