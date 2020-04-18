def won_to_korean(num):
    num = num.replace(',',"")
    print(num[:-5] + "억" + num[-5:-1] + "만원")
    return num[:-5] + "억" + num[-5:-1] + "만원"



num1 = "-57,7019"
num2 = "1977,128"

won_to_korean(num1)
won_to_korean(num2)
# a = "-123"

# b = -123
# print(a[0])
# print(b[0])

# function numberToKorean(number){
#     var inputNumber  = number < 0 ? false : number;
#     var unitWords    = ['', '만', '억', '조', '경'];
#     var splitUnit    = 10000;
#     var splitCount   = unitWords.length;
#     var resultArray  = [];
#     var resultString = '';
#
#     for (var i = 0; i < splitCount; i++){
#          var unitResult = (inputNumber % Math.pow(splitUnit, i + 1)) / Math.pow(splitUnit, i);
#         unitResult = Math.floor(unitResult);
#         if (unitResult > 0){
#             resultArray[i] = unitResult;
#         }
#     }
#
#     for (var i = 0; i < resultArray.length; i++){
#         if(!resultArray[i]) continue;
#         resultString = String(resultArray[i]) + unitWords[i] + resultString;
#     }
#
#     return resultString;
# }