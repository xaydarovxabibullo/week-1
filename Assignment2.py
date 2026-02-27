class1 = input("Class 1 name: ")
fee1 = float(input("Class 1 fee: ")) 
class2 = input("Class 2 name: ")
fee2 = float(input("Class 2 fee: "))
class3 = input("Class 3 name: ")
fee3 = float(input("Class 3 fee: "))

subtotal = fee1 + fee2 + fee3
premium_discount = subtotal * 0.22
after_discount = subtotal - premium_discount
registration_fee = after_discount * 0.13
premium61 = after_discount
premium59 = subtotal
nopremiup61 = after_discount + registration_fee




premium = input("Are you premium member (yes/no): ")

print("------- Monthly Statement -------")
print(f"{class1}                    {fee1} ")
print(f"{class2}                    {fee2}")
print(f"{class3}                    {fee3}")

print("--------------------------------")
print(f"Subtotal:                       ${subtotal}")

if subtotal >= 60 and premium == "yes":
    print(f"Premium discount (22%)         -${premium_discount}")
    print(f"After discount                  ${after_discount}")
    print(f"Registration fee (13%)          $0")
elif subtotal >= 60 and premium == "no":
    print(f"Premium discount (22%)         -${premium_discount}")
    print(f"After discount                  ${after_discount}")
    print(f"Registration fee (13%)          ${registration_fee}")
elif subtotal <= 60 and premium == "yes":
    print(f"Premium discount (22%)          $0")
    print(f"After discount                  ${subtotal}")
    print(f"Registration fee (13%)          $0")

else:
    print(f"Premium discount (22%)          $0")
    print(f"After discount                  ${subtotal}")
    print(f"Registration fee (13%)          ${registration_fee}")

print("--------------------------------")
if subtotal >= 60 and premium == "yes":
    print(f"Total                           ${premium61}")
    print("--------------------------------")
    print("Discount applied : True")
    print("Fee applied      : False")
elif subtotal <= 60:
    print(f"Total                           ${premium59}")
    print("--------------------------------")
    print("Discount applied : False")
    print("Fee applied      : False")
elif subtotal >= 60 and premium == "no":
    print(f"Total                           ${nopremiup61}")
    print("--------------------------------")
    print("Discount applied : True")
    print("Fee applied      : True")