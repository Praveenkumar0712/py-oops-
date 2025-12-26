class mobilepho:
    def __init__(spec,Mobilename,Mobilecolor,Mobileram,Mobilesize):
        spec.Mobilename=Mobilename
        spec.Mobilecolor=Mobilecolor
        spec.Mobileram=Mobileram
        spec.Mobilesize=Mobilesize
    def display(spec):
        print(f"Mobilename:{ spec.Mobilename}\n Mobilecolor:{ spec.Mobilecolor}\n Mobileram:{spec.Mobilesize} ")
a=mobilepho("oppo","grey",8,6.5,)
print(a.Mobilename,a.Mobilecolor,a.Mobileram,a.Mobilesize)
a.display()
