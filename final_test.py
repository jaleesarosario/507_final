import unittest
from final.py import *

#Finish if you can... stop crying
class TestFlora(unittest.TestCase):

    def test_colors(self):
        """
        Test colors
        """
        self.assertTrue(baseurl == 'http://researcharchive.calacademy.org')
        self.assertTrue(header == {'User-agent': 'Mozilla/5.'})
        self.assertTrue(page_soup == BeautifulSoup(page_text,'html.parser'))
        self.assertTrue(wfresults == page_soup.findAll(True, {'class':["wfresultname"]}))

        self.assertFalse(white_wf == baseurl + '/research/botany/wildflow/color.asp?c=' + item)
        self.assertFalse(wf == baseurl + '/research/botany/wildflow/color.asp?c=' + color)
        self.assertFalse(page_soup2 == requests.get(white_wf, headers=header).text)

    def test_databases(self):
        """
        Test data
        """
        self.assertTrue(color_ID == ['Color', 'Common Name', 'Family Name', 'Latin Name', 'Description'])
        self.assertTrue(writer == csv.writer(f))

        
    def test_db(self):
        """
        Test DB
        """
        self.assertEqual(DBNAME is 'Floral.db')

if __name__ == '__main__':
    unittest.main()
