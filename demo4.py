def tubiao(): 
    global clean_results
    clean_results = []
    for res in results:
        if res not in stopwords:
            clean_results.append(res)
    c = Counter(clean_results)
    clean = dict(c.most_common(6))
    key = clean.keys()
    value = clean.values()
    plt.bar(key,height=value)
    plt.xticks(np.arange(len(key)),key)
    plt.figtext(0.9 , 0.1 , '$words$')
    plt.figtext(0.1, 0.9, '$numbers$')
    plt.show()

def back1():
    window.deiconify()
    window3.destroy()

def table():
    clean_results = []
    for res in results:
        if res not in stopwords:
            clean_results.append(res)
    c = Counter(clean_results)
    clean = dict(c.most_common(6))

    window.withdraw()
    global window3
    window3 = Toplevel()
    window3.title('词频统计表')
    window3.geometry('360x320')
    frame = Frame(window3)
    frame.place(x = 20, y = 60, width = 340, height = 320)
    scrollbar = ttk.Scrollbar(frame)
    scrollbar.grid(row = 0, column = 2, sticky = NS)
    tree = ttk.Treeview(frame, columns = ("c1","c2"),show = "headings", yscrollcommand=scrollbar.set)
    tree.column('c1', width=155, anchor='center')
    tree.column('c2', width=155, anchor='center')
    tree.heading('c1', text='单词')
    tree.heading('c2', text='频率')

    tree.grid(row = 0, column = 0, columnspan = 2, sticky = W)
    scrollbar.config(command=tree.yview)
    
    for i in clean:
        tree.insert("", "end", values = (i, clean[i]))

    b5 = ttk.Button(window3,text='最高词频统计图',command=tubiao)
    b5.grid(row = 0, column = 0, padx = 40, pady = 20)

    b7 = ttk.Button(window3,text='返回',command=back1)
    b7.grid(row = 0, column = 1, padx = 40, pady = 20)

    window3.protocol("WM_DELETE_WINDOW", window.destroy)
    window3.mainloop()
    

window = Tk()
window.title('简易的文本编辑器')
window.geometry('400x440')

frame = ttk.Frame(window)
frame.place(x = 20, y = 100, width = 360, height = 320)   
scrollbar = ttk.Scrollbar(frame)
scrollbar.pack(side = RIGHT, fill = Y)

t = Text(frame,yscrollcommand=scrollbar.set)
t.pack(expand = YES, fill = BOTH)
with open('The Making of Isaac Newton.txt') as f:
    text = f.read()
t.insert('end',text)
scrollbar.config(command=t.yview)
