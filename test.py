import unittest, main, functools, random, time


class Test(unittest.TestCase):
    def setUp(self):
        self.data = [1, 7, 4, 2, 8, 4, 54, 123, 6653, 123]
        self.datax1000 = [random.randint(-10000, 10000) for i in range(10000)]

    def test_read(self):  # свой тест на проверку правильности файла (должны быть только int значения)
        self.assertTrue(all(map(lambda x: type(x) is int, main.rfile('file'))))

    def test_min(self):
        self.assertEqual(min(self.data), main.mn(self.data))
        st_time = time.time()
        main.mn(self.data)
        total_time = time.time() - st_time
        st_timex2 = time.time()
        main.mn(self.datax1000)
        total_timex2 = time.time() - st_timex2
        self.assertGreater(total_timex2, total_time)

    def test_max(self):
        self.assertEqual(max(self.data), main.mx(self.data))
        st_time = time.time()
        main.mx(self.data)
        total_time = time.time() - st_time
        st_timex2 = time.time()
        main.mx(self.datax1000)
        total_timex2 = time.time() - st_timex2
        self.assertGreater(total_timex2, total_time)

    def test_sum(self):
        self.assertEqual(sum(self.data), main.summa(self.data))
        st_time = time.time()
        main.summa(self.data)
        total_time = time.time() - st_time
        st_timex2 = time.time()
        main.summa(self.datax1000)
        total_timex2 = time.time() - st_timex2
        self.assertGreater(total_timex2, total_time)

    def test_comp(self):
        self.assertEqual(functools.reduce(lambda x, y: x * y, self.data), main.composition(self.data))
        self.assertEqual(sum(self.data), main.summa(self.data))
        st_time = time.time()
        main.composition(self.data)
        total_time = time.time() - st_time
        st_timex2 = time.time()
        main.composition(self.datax1000)
        total_timex2 = time.time() - st_timex2
        self.assertGreater(total_timex2, total_time)

    def test_readtime(self):
        with open('f1.txt', 'w', encoding='utf-8') as f:
            f.write(' '.join(map(str, self.datax1000)))
        st_time = time.time()
        main.rfile('file')
        total_time = time.time() - st_time
        st_time2 = time.time()
        main.rfile('f1.txt')
        total_time_2 = time.time() - st_time2
        self.assertGreater(total_time_2, total_time)




if __name__ == '__main__':
    unittest.main()
