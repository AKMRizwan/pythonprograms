l1=["chawal","bhindi","chowmin","aata","daal","daliya"]
# i=1
# for item in l1:
#     if i%2 is not 0:
#         print(f"please buy {item}")
#     i += 1
for index, item in enumerate(l1):
    if index%2==0:
        print(f"please buy {item}")
