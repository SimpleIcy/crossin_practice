

class MedalsInfo:
    def __init__(self, country, gold, sliver, bronze):
        self.country = country
        self.gold = gold
        self.sliver = sliver
        self.bronze = bronze

    def add_modal(self, modal):
        if modal == 'gold':
            self.gold += 1
        elif modal == 'sliver':
            self.sliver += 1
        elif modal == 'bronze':
            self.bronze += 1
        else:
            print('Type in data should be like this:   MODAL_TYPE\n\
            MODAL_TYPE include gold,sliver, bronze.or the first letter in lowercase')

    def count(self):
        return self.gold + self.sliver + self.bronze

    def __str__(self):
        return f" Country: {self.country}\tGold: {self.gold}\t Sliver: {self.sliver}\t Bronze: {self.bronze}"


# initialize data
china = MedalsInfo('china', 29, 20, 13)
usa = MedalsInfo('USA', 17, 24, 10)
india = MedalsInfo('India', 18, 14, 9)

# add modals
china.add_modal('gold')
china.add_modal('sliver')
usa.add_modal('sliver')
india.add_modal('bronze')

all_list = [china, usa, india]
# sorted all modals
order_by_sum = sorted(all_list, key=lambda x: x.count(), reverse=True)
# sorted gold modals
order_by_gold = sorted(all_list, key=lambda x: x.gold, reverse=True)

# print the order
print('\t\t\t奖牌总数榜\t\t\t')
for i in order_by_sum:
    print(i)
print('\t\t\t金牌榜\t\t\t')
for i in order_by_gold:
    print(i)



