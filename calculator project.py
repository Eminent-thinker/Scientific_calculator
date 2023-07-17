from tkinter import * 
import math as M
from time import strftime

def sin():
    sine = eval(entry.get())
    sinee = M.sin(M.radians(sine))
    entry.delete(0, END)
    entry.insert(0, 'sin({}) = {:.4f}'.format(sine, sinee))
    
 
    
def cos():
    cos = eval(entry.get())
    cosine = M.cos(M.radians(cos))
    entry.delete(0, END)
    entry.insert(0, 'cos({}) = {:.4f}'.format(cos, cosine))

    
def tan():
    tan = eval(entry.get())
    tangent = M.tan(M.radians(tan))
    entry.delete(0, END)
    entry.insert(0, 'tan({}) = {:.4f}'.format(tan, tangent))

def asin():
    arsin= eval(entry.get())
    arcsine = M.degrees(M.asin((arsin)))
    entry.delete(0, END)
    entry.insert(0, 'sin⁻¹({}) = {:.4f}'.format(arsin, arcsine))
    
def acos():
    arcos= eval(entry.get())
    arc_cos = M.degrees(M.acos((arcos)))
    entry.delete(0, END)
    entry.insert(0, 'cos⁻¹({}) = {:.4f}'.format(arcos, arc_cos))
    
def atan():
    artan= eval(entry.get())
    arctan = M.degrees(M.atan((artan)))
    entry.delete(0, END)
    entry.insert(0, 'tan-¹({}) = {:.4f}'.format(artan, arctan))
    
def pow():
    p = entry.get()
    if ',' in p:
        p = p.split(',')
        list =[]
        for x in p:
            y = eval(x)
            list.append(y)
            entry.delete(0, END)
        entry.insert(0, '{}^{} = {}'.format(list[0], list[1],M.pow(list[0], list[1])))

def pi():
        entry.insert(0, '{} = {:4f}'.format('π', M.pi))
        
def fact():
    f = eval(entry.get())
    entry.delete(0,END)
    entry.insert(0, '{}{} = {}'.format(f, '!', M.factorial(f)))

def sqrt():
       s = eval(entry.get())
       entry.delete(0, END)
       entry.insert(0,'{}({}) = {}'.format('√', s, M.sqrt(s)))
       
def sq():
       s = eval(entry.get())
       q = s**2
       entry.delete(0, END)
       entry.insert(0, '{}{} = {}'.format(s, '²', q))

def log10(): # natural logarithms
        l = eval(entry.get()) 
        entry.delete(0, END)     
        entry.insert(0,'{}{} = {}'.format('log₁₀', l, M.log10(l)))  
        
def log2(): # log of base 2
       g = eval(entry.get())
       entry.delete(0, END)
       entry.insert(0,'{}{} = {}'.format('log₂', g, M.log2(g)))
       
def exp(): # exponential function
         x = eval(entry.get())
         entry.delete(0, END)   
         entry.insert(0, '{}^{} = {}'.format('e', x, M.exp(x)))       
                     
def num_0(): # displaying 0 on entrybox
      entry.insert(99,'0')
   
def num_1(): # displaying 1 on entrybox
      entry.insert(99,'1')
   
def num_2(): # displaying 2 on entrybox
      entry.insert(99,'2')
      
def num_3(): # displaying 3 on entrybox
      entry.insert(99,'3')
      
def num_4(): # displaying 4 on entrybox
      entry.insert(99,'4')
      
def num_5(): # displaying 5 on entrybox
      entry.insert(99,'5')
      
def num_6(): # displaying 6 on entrybox
      entry.insert(99,'6')
      
def num_7(): # displaying 7 on entrybox
      entry.insert(99,'7')
      
def num_8(): # displaying 8 on entrybox
      entry.insert(99,'8')
      
def num_9(): # displaying 9 on entrybox
      entry.insert(99,'9')

def dot(): # displaying dot on entrybox
      entry.insert(99,'.')

def coma(): # displaying coma on entrybox
      entry.insert(99, ',')      
      
def CLR():
      entry.delete(entry.index(END)-1)
   
def BCK():
       entry.delete(0, END)
       
def calculate():
    calc = entry.get()
    if '+' in calc:
      calc = calc.split('+')
      list =[]
      for x in calc:
        y = eval(x)
        list.append(y)
        entry.delete(0,END)
        entry.insert(0, sum(list))
    elif '-' in calc:
      calc = calc.split('-')
      list = []
      for x in calc:
        y = eval(x)
        list.append(y)
        entry.delete(0, END)
      entry.insert(0,list[0]-list[1])
    elif '×' in calc:
      calc = calc.split('×')
      multiply =1
      for x in calc:
        y = eval(x)
        multiply *= y
        entry.delete(0, END)
      entry.insert(0, multiply)
    
    else:
      calc = calc.split('÷')
      list =[]
      for x in calc:
        y = eval(x)
        list.append(y)
        entry.delete(0, END)
      entry.insert(0,list[0]/list[1])
 
def div(): # displaying ÷ on entrybox
       entry.insert(99, '÷')
       
def mul(): # displaying × on entrybox
       entry.insert(99, '×')
    
def sub(): # displaying minus on entrybox
       entry.insert(99, '-')
       
def add(): # displaying + on entrybox
       entry.insert(99, '+')
root = Tk()
entry= Entry(font = ('Verdana', 16, 'bold'))
entry.grid(row=1, column=0, columnspan=150, ipadx=168, ipady=70)
time_label = Label( font = ('calibri', 25, 'bold'))
def clock():
        time_label.configure(text = strftime("%I:%M:%S%p"))
        time_label.after(1000, clock)
clock()
time_label.grid(row= 0, column = 0, columnspan = 4)

sine_button= Button(text ="sin(x)", padx=42, command = sin)

cosine_button=Button(text="cos(x)", padx=42, command= cos)

tangent_button= Button(text="tan(x)", padx=48, command=tan)

arcsine_button = Button(text="sin-¹(x)", padx=31, command=asin)

arc_cosine_button = Button(text = 'cos-¹(x)', padx =31, command = acos)

arctan_button = Button(text = 'tan-¹(x)', padx = 37, command = atan)

pow_button = Button(text= 'xʸ', padx = 68, command = pow)
pi_button = Button(text = 'π', padx = 80, command = pi)
fact_button = Button(text = '!', padx= 127, command = fact)
sqrt_button = Button(text = '√x', padx = 69, command = sqrt)
sq_button = Button(text = 'x²', padx = 68, command = sq)
log10_button = Button(text = 'log₁₀ˣ', padx =48, command = log10)
log2_button = Button(text = 'log₂ˣ', padx = 96, command = log2)
exp_button = Button(text = 'e', padx = 79, command = exp)
sine_button.grid(row=2, column=0, ipady = 15)
cosine_button.grid(row=2, column=1, ipady = 15)
tangent_button.grid(row=2, column=2, ipady = 15)
arcsine_button.grid(row=3, column=0, ipady = 15)
arc_cosine_button.grid(row=3, column=1, ipady = 15)
arctan_button.grid(row=3, column=2, ipady = 15)
pow_button.grid(row=4, column = 0, ipady = 15)
pi_button.grid(row =4, column = 2, ipady = 15)
fact_button.grid(row = 4, column = 3, ipady = 15)
sqrt_button.grid(row = 5, column = 1, ipady = 15)
sq_button.grid(row = 5, column = 0, ipady = 15)
log10_button.grid(row = 5, column = 2, ipady = 15)
log2_button.grid(row = 5, column = 3, ipady = 15)
exp_button.grid(row = 4, column = 1, ipady = 15)
clear_button = Button( text= 'DEL', padx=102, command =CLR ).grid(row=2, column=3, ipady = 15)
back_button = Button(text='AC', padx =110, command = BCK).grid(row=3, column= 3, ipady = 15)
button_0 = Button( text= '0', padx=73, command =num_0 ).grid(row=9, column=0, ipady = 30)
button_1 = Button( text= '1', padx=73, command =num_1 ).grid(row=8, column=0, ipady = 30)
button_2 = Button( text= '2', padx=77, command =num_2 ).grid(row=8, column=1, ipady = 30)
button_3 = Button( text= '3', padx=80, command =num_3 ).grid(row=8, column=2, ipady = 30)
button_4 = Button( text= '4', padx=73, command =num_4 ).grid(row=7, column=0, ipady = 30)
button_5 = Button( text= '5', padx=77, command =num_5 ).grid(row=7, column=1, ipady = 30)
button_6 = Button( text= '6', padx=80, command =num_6 ).grid(row=7, column=2, ipady = 30)
button_7 = Button( text= '7', padx=73, command =num_7 ).grid(row=6, column=0, ipady = 30)
button_8 = Button( text= '8', padx=77, command =num_8 ).grid(row=6, column=1, ipady = 30)
button_9 = Button( text= '9', padx=80, command =num_9 ).grid(row=6, column=2, ipady = 30)
dot_button = Button(text = '.', padx= 82, command = dot).grid(row = 9, column = 1, ipady = 30)
coma_button = Button(text = ',', padx=86, command = coma).grid(row=9, column=2, ipady = 30)
calc_button = Button(text='=', padx= 145, command=calculate ).grid(row=10, column=0, columnspan = 4, ipadx = 250, ipady = 40)
div_button = Button(text= '÷', padx = 122, command = div ).grid(row=6, column=3, ipady = 30)
mul_button = Button(text= '×', padx = 122, command= mul ).grid(row=7, column=3, ipady = 30)
sub_button = Button(text= '-', padx = 126, command = sub ).grid(row=8, column=3, ipady = 30)
add_button = Button(text= '+', padx = 122, command = add ).grid(row=9, column=3, ipady = 30)

mainloop()