def numberToKorean(input):
        input = str(input)
        if str(input)[0] == "-":
            print("-입니다.")
            input = input[1:]
            print(input)
        else:
            print("+입니다.")
            print(input)



numberToKorean("-1234")
numberToKorean("123")

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