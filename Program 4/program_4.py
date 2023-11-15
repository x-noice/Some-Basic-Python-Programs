original_cost = eval(input('Enter the original cost of the goods:\n₹'))
gst_rate = eval(input('Enter the gst rate %: \n'))
gst_amount = (original_cost * gst_rate)/100
total_amt = original_cost + gst_amount
print('Total amount is ₹', total_amt, sep = '')
