import ApplyFilter as ap
import Printer as p
import TakePhoto as tp

def main():
    tier_cantity = 1
    filter_tier_1 = False
    if tier_cantity == 2:
        filter_tier_2 = False
        tier_2 = list()
    tier_1 = list()
    payment = True

    if payment:
            
        for i in range(5):    
            
            image = tp.take_photo(i)
                
            if tier_cantity == 2:
                image_2 = image
                image_2 = ap.apply_filter(image_2, filter_tier_2)
                tier_2.append(image_2)
                    
            image = ap.apply_filter(image, filter_tier_1)
            tier_1.append(image)
        
            take_again = True
        
            if take_again:
                tp.take_photo(i)