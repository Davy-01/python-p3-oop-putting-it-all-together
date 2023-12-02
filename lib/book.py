#!/usr/bin/env python3

class Book:
    def __init__(self, title, page_count):
        self.title = title
        self._page_count = page_count
        self.current_page=1
    
    def get_page(self):
        return self._page_count

    def set_page(self,page_count):
        if type(page_count)==int:
            self._page_count=page_count
            print("Getting the page book number")
        else:
            print("page_count must be an integer")

    page_count=property(get_page, set_page)

    def turn_page(self):
        if self.current_page < self.page_count:
            print("Flipping the page...wow, you read fast!")
            self.current_page+=1
        else:
            print("You've reached the end of the book")
        

        