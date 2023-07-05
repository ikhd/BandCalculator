import tkinter as tk
import webbrowser

def calculate_bands():
    result = ""
    try:
        band_input = entry.get()
        bands = [int(band.strip()) for band in band_input.split("+")]
        m_values = []
        k_values = []

        for band in bands:
            m = 0
            k = ""
            if band > 64:
                k = (band - 64) - 1
                k = 2 ** k
                k = format(k, 'X')  # Format as hexadecimal without '0x' prefix
            lband = band
            x = lband - 1
            bband = 2 ** x
            mr1 = "AT!Band=04,\"B{}\",0,{},0,0,0,0".format(lband, format(bband, 'X'))  # Format as hexadecimal without '0x' prefix
            result += "{},{}\n".format(mr1, k)
            m_values.append(bband)
            k_values.append(k)

        bbands_sum = sum(m_values)
        k_sum = sum(int(k, 16) for k in k_values if k.startswith("0x"))  # Convert to int only if it starts with "0x"

        result += "\nكود الدمج:\n\nAT!Band=04,\"{}\",0,{},0,0,0,0\n".format("+".join(["B{}".format(b) for b in bands]), format(bbands_sum, 'X'))  # Format as hexadecimal without '0x' prefix

        result_text.delete(1.0, tk.END)  # Clear previous result
        result_text.insert(tk.END, result)

        # Adjust window size based on the result text length
        lines = len(result.split('\n'))
        result_text_height = 20
        root.geometry("400x{}".format(300 + lines * result_text_height))

    except ValueError:
        result_text.delete(1.0, tk.END)  # Clear previous result
        result_text.insert(tk.END, "خطأ في التطبيق، تأكد من كتابة الرقم الصحيح")

def exit_program():
    root.destroy()

def open_twitter():
    webbrowser.open("https://twitter.com/REMiX_KSA")

def open_telegram():
    webbrowser.open("https://t.me/xrouter_group")

root = tk.Tk()
root.title("4G حاسبة الترددات")

label1 = tk.Label(root, text="+الرجاء كتابة رقم التردد، في حالة وجود أكثر من تردد يجب الفصل بينهم بعلامة")
label2 = tk.Label(root, text="كمثال : 1+3")
label1.pack()
label2.pack()

entry = tk.Entry(root)
entry.pack()

calculate_button = tk.Button(root, text="حساب التردد", command=calculate_bands)
calculate_button.pack()

button_frame = tk.Frame(root)
button_frame.pack()

twitter_button = tk.Button(button_frame, text="التويتر", command=open_twitter)
twitter_button.pack(side=tk.LEFT)

telegram_button = tk.Button(button_frame, text="عالم الراوترات", command=open_telegram)
telegram_button.pack(side=tk.LEFT)

exit_button = tk.Button(root, text="خروج", command=exit_program)
exit_button.pack()

label3 = tk.Label(root, text="By: Khalid | Tw: @REMiX_KSA")
label3.pack()

result_text = tk.Text(root)
result_text.pack()

root.mainloop()
