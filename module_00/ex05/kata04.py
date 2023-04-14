# Put this at the top of your kata04.py file
kata = (0, 4, 132.42222, 10000, 12345.67)
kata2 = (11, 42, 132.42222, 654123, 12345.67)
kata0 = (0,0,0,0,0)

(module, ex, *value) = kata
print(f"module_{'{:02d}'.format(module)}, ex_{'{:02d}'.format(ex)} : {'{:.2f}'.format(value[0])}, {'{:.2e}'.format(value[1])}, {'{:.2e}'.format(value[2])}")

# (module, ex, *value) = kata2
# print(f"module_{'{:02d}'.format(module)}, ex_{'{:02d}'.format(ex)}: {'{:.2f}'.format(value[0])}, {'{:.2e}'.format(value[1])}, {'{:.2e}'.format(value[2])}")

# (module, ex, *value) = kata0
# print(f"module_{'{:02d}'.format(module)}, ex_{'{:02d}'.format(ex)}: {'{:.2f}'.format(value[0])}, {'{:.2e}'.format(value[1])}, {'{:.2e}'.format(value[2])}")