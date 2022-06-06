from seleniumbase import BaseCase


class CarInfo(BaseCase):

    def setUp(self):
        super().setUp()
        self.open("https://bitfax.info/")

    def tearDown(self):
        self.delete_all_cookies()
        super().tearDown()

    def test_get_cars_data(self):
        self.click("(//img[contains(@class,'xfieldimage skrin')])[1]")
        elems = self.find_elements("div[class='fotorama__thumb fotorama__loaded fotorama__loaded--img']")
        qty = len(elems)
        print(qty)
        for i in range(qty):
            a = self.get_image_url("(//img[@class='fotorama__img'])")
            self.sleep(0.5)
            self.download_file(a, destination_folder="./cars")
            self.click(".fotorama__arr.fotorama__arr--next")