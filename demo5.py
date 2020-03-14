
def back4():
    window.deiconify()
    window5.destroy()

def text_done():
    with open('The Making of Isaac Newton.txt') as f:
        text = f.read()
    text = text.replace('\n',' ').replace(',',' ').replace('.',' ')
    words = []
    infos = text.split(' ')
    for info in infos:
        if str(info).isalpha():
            words.append(str(info).lower())
    window.withdraw()
    global window5
    window5 = Toplevel()
    window5.title('处理后的文本')
    window5.geometry('400x420')

    frame1 = ttk.Frame(window5)
    frame1.place(x = 20, y = 30, width = 360, height = 330)   
    scrollbar1 = ttk.Scrollbar(frame1)
    scrollbar1.pack(side = RIGHT, fill = Y)

    t1 = Text(frame1,yscrollcommand=scrollbar1.set)
    t1.pack(expand = YES, fill = BOTH)
    t1.insert('end',words)
    scrollbar1.config(command=t1.yview)
    b9 = ttk.Button(window5,text='返回',command=back4)
    b9.grid(row = 0, column = 1, padx = 240, pady = 380)

    window5.protocol("WM_DELETE_WINDOW", window.destroy)
    window5.mainloop()



def back2():
    window.deiconify()
    window1.destroy()
def count():
    window.withdraw()
    global window1
    window1 = Toplevel()
    window1.title('词频')
    window1.geometry('300x180')
    
    results = read()
    var = str(len(list(set(results))))
    Label(window1, text = u"单词数量是：", font = Font).grid(padx = 20, pady = 40)
    t1 = Label(window1,text = var, font = Font)
    t1.grid(row = 0, column = 1, padx = 0, pady = 40)

    b6 = ttk.Button(window1,text='返回',command=back2)
    b6.grid(row = 1, column = 1, padx = 0, pady = 20)


    window1.protocol("WM_DELETE_WINDOW", window.destroy)
    window1.mainloop()


def keywords():
    window.withdraw()
    window2 = Toplevel()
    window2.title('最高词频')
    window2.geometry('400x400')
    
    with open('The Making of Isaac Newton.txt') as f:
        text = f.read()
    text = text.replace('\n',' ').replace(',',' ').replace('.',' ')
    words = []
    infos = text.split(' ')
    for info in infos:
        if info != '':
            words.append(info)
    c = dict(Counter(words).most_common(6))
    var = list(c.keys())
    var = '\n'.join(var)
    print(c)
    
    t1 = Text(window2,height=10,width=10,font=('simhei',16))
    t1.pack()
    t1.insert('end',var)
    window2.protocol("WM_DELETE_WINDOW", window.destroy)
    window2.mainloop()

b1 = ttk.Button(window,text='单词个数统计',command=count)
b1.grid(row = 0, column = 0, padx = 20, pady = 18)

b2 = ttk.Button(window,text='最高词频统计表',command=table)
b2.grid(row = 0, column = 1, padx = 20, pady = 18)

b3 = ttk.Button(window,text='词频统计',command=word_times)
b3.grid(row = 0, column = 2, padx = 20, pady = 18)

b4 = ttk.Button(window,text='点击此处进行文本处理',command=text_done)
b4.grid(row = 1, column = 0, columnspan = 3, padx = 20, pady = 0, ipadx = 50)

window.mainloop()
