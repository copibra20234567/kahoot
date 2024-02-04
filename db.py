from kpopfignya import SQLManager
sql = SQLManager("kahoot.db")
sql.create_tables()
sql.add_quizz("Україна", "Квіз про Україну")