import pandas as tonystark
import numpy as BruceBanner
import matplotlib.pyplot as steverogers




print("""--------------------------------MODERN PERIODIC TABLE---------------------------""")
print('\n')

print("""________________________________________________________________________________
                        1. Details of Element of periodic table 
                                2.Generate the graph
                                3. About Project
                                4. Contact us                                            """)
print('\n')
A = int(input("Enter the from above given option  :"))






def au():
    while True:
        
        def display_periodic_table(element):
            print()
            print()
            print("                     --------- MODERN PERIODIC TABLE -----------             \n\n")
            print("┌────┐                                                                               ┌────┐")
            print("│ {0}  │                                                                               │ {1} │".format(element[1],element[2]))
            print("├────┼────┐                                                 ┌────┬────┬────┬────┬────┼────┤")
            print("│ {0} │ {1} │                                                 │ {2}  │ {3}  │ {4}  │ {5}  │ {6}  │ {7} │".format(element[3],element[4],element[5],element[6],element[7],element[8],element[9],element[10]))
            print("├────┼────┤                                                 ├────┼────┤────┼────┤────┼────┤")
            print("│ {0} │ {1} │                                                 │ {2} │ {3} │ {4}  │ {5}  │ {6} │ {7} │".format(element[11],element[12],element[13],element[14],element[15],element[16],element[17],element[18]))
            print("├────┼────┼────┬────┬────┬────┬────┬────┬────┬────┬────┬────┼────┼────┼────┼────┼────┼────┤")
            print("│ {0}  │ {1} │ {2} │ {3} │ {4}  │ {5} │ {6} │ {7} │ {8} │ {9} │ {10} │ {11} │ {12} │ {13} │ {14} │ {15} │ {16} │ {17} │".format(element[19],element[20],element[21],element[22],element[23],element[24],element[25],element[26],element[27],element[28],element[29],element[30],element[31],element[32],element[33],element[34],element[35],element[36]))
            print("├────┼────┼────┼────┼────┼────┼────┼────┼────┼────┼────┼────┼────┼────┼────┼────┼────┼────┤")
            print("│ {0} │ {1} │ {2}  │ {3} │ {4} │ {5} │ {6} │ {7} │ {8} │ {9} │ {10} │ {11} │ {12} │ {13} │ {14} │ {15} │ {16}  │ {17} │".format(element[37],element[38],element[39],element[40],element[41],element[42],element[43],element[44],element[45],element[46],element[47],element[48],element[49],element[50],element[51],element[52],element[53],element[54]))
            print("├────┼────┼────┼────┼────┼────┼────┼────┼────┼────┼────┼────┼────┼────┼────┼────┼────┼────┤")
            print("│ {0} │ {1} │{2}│ {3} │ {4} │ {5}  │ {6} │ {7} │ {8} │ {9} │ {10} │ {11} │ {12} │ {13} │ {14} │ {15} │ {16} │ {17} │".format(element[55],element[56],"LaLu",element[72],element[73],element[74],element[75],element[76],element[77],element[78],element[79],element[80],element[81],element[82],element[83],element[84],element[85],element[86]))
            print("├────┼────┼────┼────┼────┼────┼────┼────┼────┼────┼────┼────┼────┼────┼────┼────┼────┼────┤")
            print("│ {0} │ {1} │{2}│ {3} │ {4} │ {5} │ {6} │ {7} │ {8} │ {9} │ {10} │ {11} │ {12}│ {13}│ {14}│ {15}│ {16}│ {17}│".format(element[87],element[88],"AcLr",element[104],element[105],element[106],element[107],element[108],element[109],element[110],element[111],element[112],element[113],element[114],element[115],element[116],element[117],element[118]))
            print("└────┴────┴────┴────┴────┴────┴────┴────┴────┴────┴────┴────┴────┴────┴────┴────┴────┴────┘")
            print()
            print("       ┌────┬────┬────┬────┬────┬────┬────┬────┬────┬────┬────┬────┬────┬────┬────┐")
            print("       │ {0} │ {1} │ {2} │ {3} │ {4} │ {5} │ {6} │ {7} │ {8} │ {9} │ {10} │ {11} │ {12} │ {13} │ {14} │".format(element[57],element[58],element[59],element[60],element[61],element[62],element[63],element[64],element[65],element[66],element[67],element[68],element[69],element[70],element[71]))
            print("       ├────┼────┼────┼────┼────┼────┼────┼────┼────┼────┼────┼────┼────┼────┼────┤")
            print("       │ {0} │ {1} │ {2} │ {3}  │ {4} │ {5} │ {6} │ {7} │ {8} │ {9} │ {10} │ {11} │ {12} │ {13} │ {14} │".format(element[89],element[90],element[91],element[92],element[93],element[94],element[95],element[96],element[97],element[98],element[99],element[100],element[101],element[102],element[103]))
            print("       └────┴────┴────┴────┴────┴────┴────┴────┴────┴────┴────┴────┴────┴────┴────┘")
            print()
            print()

        data = tonystark.read_csv("atomic_data.csv")















        data.head()



        data.shape


        l = data['element_symbol'].to_list()
        l.insert(0, "")

        display_periodic_table(l)
    
    
        atom = input("Enter the Atomic Symbol : ").capitalize()
        indx = data.index[data['element_symbol']== atom].tolist()[0]
        print("----------------------------"),
        print("\tDescription")
        print("----------------------------")
        print("Atomic Number          : ",data['atomic_number'][indx])
        print("Atomic Symbol          : ",data['element_symbol'][indx])
        print("Atomic mass            : ",data['atomic_mass'][indx])
        print("Nutron                 : ",data['nutron'][indx])
        print("Proton                 : ",data['proton'][indx])
        print("Element Name           : ",data['element_name'][indx])
        print("Property               : ",data['property'][indx])
        print("Melting point          : ",data['melting_point'][indx])
        print("Boiling point          : ",data['boiling_point'][indx])
        print("Discovery              : ",data['discovery'][indx])
        print("Group                  : ",data['group'][indx])
        print("ELECTRON CONFIGURATION : ",data['ELECTRON_CONFIGURATION'][indx])
        print("Ionization Rnergy      : ",data['ionization_energy'][indx])





        print("┌────┐")
        print("│ {0} │".format(atom))
        print("├────┼")

def ay():
    print("1.Line Graph ")
    print("2.Bar Graph " )
    print('\n')
    b = int(input("Enter which graph you want to see :-) "))
    def line():
        
        print("1.melting point")
        print("2.boiling point")
        print("3.atomic mass")
        print("4.ionization energy")
        print('\n')
        c = int(input("Enter which graph you want to see :-) "))
        
        def MP():
            data = tonystark.read_csv("atomic_data.csv",usecols = ['element_symbol','melting_point'])
            steverogers.ylabel("melting point")
            steverogers.xlabel("Atomic Symbol")
            steverogers.title("melting point ")
            steverogers.grid(True)
            steverogers.plot(data["element_symbol"],data["melting_point"],color='black')
            steverogers.show()

        def BP():
            data = tonystark.read_csv("atomic_data.csv",usecols = ['element_symbol','boiling_point'])
            steverogers.ylabel("boiling point")
            steverogers.xlabel("Atomic Symbol")
            steverogers.title("boiling point ")
            steverogers.grid(True)
            steverogers.plot(data["element_symbol"],data["boiling_point"],color ='blue'  )
            steverogers.show()

        def AM():
            data = tonystark.read_csv("atomic_data.csv",usecols = ['element_symbol','atomic_mass'])
            steverogers.ylabel("atomic mass")
            steverogers.xlabel("Atomic Symbol")
            steverogers.title("atomic mass ")
            steverogers.grid(True)
            steverogers.plot(data["element_symbol"],data["atomic_mass"],color='red')
            steverogers.show()
        
        def IE():
            data = tonystark.read_csv("atomic_data.csv",usecols = ['element_symbol','ionization_energy'])
            steverogers.ylabel("ionization energy")
            steverogers.xlabel("Atomic Symbol")
            steverogers.title("ionization energy")
            steverogers.grid(True)
            steverogers.plot(data["element_symbol"],data["ionization_energy"],color='green'  )
            steverogers.show()

        if c == 1:
             print(MP())
        elif c == 2 :
             print(BP()) 
        elif c == 3 :
             print(AM())
        elif c == 4 :
             print(IE())
             
        

    def BAR():
                
        print("1.melting point")
        print("2.boiling point")
        print("3.atomic mass")
        print("4.ionization energy")
        print('\n')
        d= int(input("Enter which graph you want to see :-) "))
        def MP():
            data = tonystark.read_csv("atomic_data.csv",usecols = ['element_symbol','melting_point'])
            steverogers.ylabel("melting point")
            steverogers.xlabel("Atomic Symbol")
            steverogers.title("melting point ")
            steverogers.grid(True)
            steverogers.bar(data["element_symbol"],data["melting_point"] ,color='black' )
            steverogers.show()

        def BP():
            data = tonystark.read_csv("atomic_data.csv",usecols = ['element_symbol','boiling_point'])
            steverogers.ylabel("boiling point")
            steverogers.xlabel("Atomic Symbol")
            steverogers.title("boiling point ")
            steverogers.grid(True)
            steverogers.bar(data["element_symbol"],data["boiling_point"],color='blue'  )
            steverogers.show()

        def AM():
            data = tonystark.read_csv("atomic_data.csv",usecols = ['element_symbol','atomic_mass'])
            steverogers.ylabel("atomic mass")
            steverogers.xlabel("Atomic Symbol")
            steverogers.title("atomic mass ")
            steverogers.grid(True)
            steverogers.bar(data["element_symbol"],data["atomic_mass"],color = 'green'  )
            steverogers.show()
        
        def IE():
            data = tonystark.read_csv("atomic_data.csv",usecols = ['element_symbol','ionization_energy'])
            steverogers.ylabel("ionization energy")
            steverogers.xlabel("Atomic Symbol")
            steverogers.title("ionization energy")
            steverogers.grid(True)
            steverogers.bar(data["element_symbol"],data["ionization_energy"],color='red'  )
            steverogers.show()

        if d == 1 :
            print(MP())
        elif d == 2 :
            print(BP()) 
        elif d == 3 :
            print(AM())
        elif d == 4 :
            print(IE())
        

    if b == 1 :
        print(line())
    elif b == 2:
        print(BAR())

def ap():
    print('\n')
    print('''
About Project -
___________________________________________________________________________________________________________________________
|This is a search engine for the detail of elements in the periodic table.                                               
|where you can find anykind of details or their properties by simply enternig the element in serach bar.                
|and this is offline search engine and also shows graph(trends of Melting point , Boiling point ,Atomic mass and Ionization energy)
|which also helps to see the trends by simply dislaying                                                                                         
___________________________________________________________________________________________________________________________''')
    

def cu():
    print('\n')
    print("""contact : please call or contact to :-)  kakadiya prachi, kakadiya mohit
                            
               Instagram :-) KP.013
                                 
                                                            
               Scanpchat :-) MK.012""")

if A == 1:
    print(au())
elif A == 2 :
    print(ay())
elif A == 3:
    print(ap())
elif A == 4:
    print(cu())
else:
    print("Please enter Number between 1-4")
