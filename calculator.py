import tkinter as tk

calculation=""

def add_to_calculation(s):
    global calculation
    calculation+=str(s)
    text_rezult.delete(1.0,"end")
    text_rezult.insert(1.0,calculation)

def evaluate_calculation():
    global calculation
    try:
        calculation=str(eval(calculation))
        text_rezult.delete(1.0,"end")
        text_rezult.insert(1.0,calculation)
    except:
        clear_field()
        text_rezult.insert(1.0,"error")


def clear_field():
    global calculation
    calculation=""
    text_rezult.delete(1.0,"end")
page = tk.Tk()
page.geometry("360x300")
text_rezult=tk.Text(page,height=2,width=16,font=("Arial",24))
text_rezult.grid(columnspan=5)
btn_1=tk.Button(page,text='1',command=lambda:add_to_calculation(1),width=5,font=('Arial'))
btn_1.grid(row=2,column=1)
btn_2=tk.Button(page,text='2',command=lambda:add_to_calculation(2),width=5,font=('Arial'))
btn_2.grid(row=2,column=2)
btn_3=tk.Button(page,text='3',command=lambda:add_to_calculation(3),width=5,font=('Arial'))
btn_3.grid(row=2,column=3)
btn_4=tk.Button(page,text='4',command=lambda:add_to_calculation(4),width=5,font=('Arial'))
btn_4.grid(row=3,column=1)
btn_5=tk.Button(page,text='5',command=lambda:add_to_calculation(5),width=5,font=('Arial'))
btn_5.grid(row=3,column=2)
btn_6=tk.Button(page,text='6',command=lambda:add_to_calculation(6),width=5,font=('Arial'))
btn_6.grid(row=3,column=3)
btn_7=tk.Button(page,text='7',command=lambda:add_to_calculation(7),width=5,font=('Arial'))
btn_7.grid(row=4,column=1)
btn_8=tk.Button(page,text='8',command=lambda:add_to_calculation(8),width=5,font=('Arial'))
btn_8.grid(row=4,column=2)
btn_9=tk.Button(page,text='9',command=lambda:add_to_calculation(9),width=5,font=('Arial'))
btn_9.grid(row=4,column=3)
btn_0=tk.Button(page,text='0',command=lambda:add_to_calculation(0),width=5,font=('Arial'))
btn_0.grid(row=5,column=2)
btn_pl=tk.Button(page,text='+',command=lambda:add_to_calculation("+"),width=5,font=('Arial'))
btn_pl.grid(row=2,column=4)
btn_min=tk.Button(page,text='-',command=lambda:add_to_calculation("-"),width=5,font=('Arial'))
btn_min.grid(row=3,column=4)
btn_div=tk.Button(page,text='/',command=lambda:add_to_calculation("/"),width=5,font=('Arial'))
btn_div.grid(row=4,column=4)
btn_equ=tk.Button(page,text='=',command=evaluate_calculation,width=13,font=('Arial'))
btn_equ.grid(row=6,column=1,columnspan=2)
btn_op=tk.Button(page,text='(',command=lambda:add_to_calculation("("),width=5,font=('Arial'))
btn_op.grid(row=5,column=1)
btn_clo=tk.Button(page,text=')',command=lambda:add_to_calculation(")"),width=5,font=('Arial'))
btn_clo.grid(row=5,column=3)
btn_dt=tk.Button(page,text='*',command=lambda:add_to_calculation("*"),width=5,font=('Arial'))
btn_dt.grid(row=5,column=4)
btn_clear=tk.Button(page,text='C',command=clear_field,width=13,font=('Arial'))
btn_clear.grid(row=6,column=3,columnspan=2)
page.mainloop()


