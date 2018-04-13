import sys
K = int( sys.stdin.readline() )
Order = list( map( int , sys.stdin.readline().split() ) )
Source = ['S1','S2','S3','S4','S5','S6','S7','S8','S9','S10','S11','S12','S13',
          'H1','H2','H3','H4','H5','H6','H7','H8','H9','H10','H11','H12','H13',
          'C1','C2','C3','C4','C5','C6','C7','C8','C9','C10','C11','C12','C13',
          'D1','D2','D3','D4','D5','D6','D7','D8','D9','D10','D11','D12','D13',
          'J1','J2']
New = [ i for i in range( 54 ) ]
for i in range( 54 ) :
    Position = Order[ i ] - 1
    for j in range( K - 1 ) :
        Position = Order[ Position ] - 1
    New[ Position ] = i
for i in range( 53 ):
    print( Source[ New [ i ] ],'',end='')
print( Source[ New[ 53 ] ])
'''思路：将下标数组Sourece第 i 个位置的元素对给定的顺序Order重复迭代K次后得到一个新的位置 P ，创建一个新数组New，将数组的 P 位置放入 i ,
最后将原始数组按全新数组New的顺序输出, 例如原题的例子中 order第一个数字为36 ,那么直接将下标 1 移到位置36，之后顺序输出时，达到第36个位置时就会输出
原数组第1个位置的元素'''
