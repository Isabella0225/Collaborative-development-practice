def word_times():
    results = read()
    c = dict(Counter(results))
    sort = sorted(c.items(),key=lambda x:x[1],reverse=True)
    sort = dict(sort)
    window.withdraw()
    global window4
    window4 = Toplevel()
    window4.title('词频统计表')
    window4.geometry('360x320')
    frame = Frame(window4)
    frame.place(x = 20, y = 20, width = 340, height = 320)
    scrollbar = ttk.Scrollbar(frame)
    scrollbar.grid(row = 0, column = 2, sticky = NS)
    tree = ttk.Treeview(frame, columns = ("c1","c2"),show = "headings", yscrollcommand=scrollbar.set)
    tree.column('c1', width=155, anchor='center')
    tree.column('c2', width=155, anchor='center')
    tree.heading('c1', text='单词')
    tree.heading('c2', text='频率')

    tree.grid(row = 0, column = 0, columnspan = 2, sticky = W)
    scrollbar.config(command=tree.yview)
    
    for i in sort:
        tree.insert("", "end", values = (i, sort[i]))

    b8 = ttk.Button(window4,text='返回',command=back3)
    b8.grid(padx = 230, pady = 270)

    window4.protocol("WM_DELETE_WINDOW", window.destroy)
    window4.mainloop()

results = read()
stopwords = []
f = open('百度停用词表.txt',encoding='utf-8')

for line in f.readlines():
    stopwords.append(line.strip())
