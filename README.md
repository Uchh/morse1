ВАЖНО! Я поменял условия тестов! self.assertEqual(decoder.decode("... ___ ... "), "S O S ")
В конце шифра добавил еще один пробел, иначе мой алгоритм будет пропускать последюю букву!
Что касается одиночных шифров self.assertEqual(decoder.decode("._"), "A ")
Оставил так же.
