Использование приложения

# 1 вариант: Подбор жилья

Пользователь указывает необходимые условия: 
- аренда или покупка жилья
- свой возраст, семейное положение, наличие и возраст детей

## Входные данные:
возраст (18-25) (26-39) (40-...)
пол (м/ж)
семейное положение (холост/не замужем) (в отношениях/в браке) (разведен/-а)
количество членов семьи (кол-во)
дети (есть/нет, если есть - кол-во)

## Рекомендации:
если возраст (18-25), пол(м), семейное положение (холост), количество членов семьи (1), детей (нет) - предлагать варианты районов с (досуг), (парки), (торговля).


Приложение на основании определенного набора параметров советует район. 

Например, зрелым семьям без детей - будет рекомендован район в котором нет (либо мало) школ/детских садов, либо район где малое количество свободных мест в учреждениях образования, но есть объекты досуга.

А молодым людям с маленькими детьми - район с наибольшим количеством мест в детских садах.

Рекомендация даётся путем окрашивания района в определенный цвет, после того как получен ответ от сервера и закончены вычисления
на стороне клиента.

# 2 вариант: Подбор объекта для застройки

На основании вычислений загруженности приложение окрашивает район на карте в цвета (зеленый, желтый, красный) указывая степень
загруженности объектов инфраструктуры в этом районе. 
Например, выбрать район и "загруженность школ" - красный. Рекомендация: строить больше школ, по аналогии с детскими садами,
торговыми площадями (магазины и торговые центры), поликлиниками.

Если все объекты инфраструктуры не загружены - значит надо искать там недвижимость (сказка, ха-ха), либо строить жилые дома.