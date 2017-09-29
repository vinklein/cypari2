# -*- coding: utf-8 -*-
# Created 09/26/2017

"""Original pari/GP test file minim :
{d=[4,2,-2,-2,2,1,-2,2,2; 2,4,-2,0,0,0,-1,0,2; -2,-2,4,2,-2,1,1,-1,-2;
-2,0,2,4,-3,1,0,-2,0; 2,0,-2,-3,4,-1,0,2,0; 1,0,1,1,-1,4,0,-1,1;
-2,-1,1,0,0,0,4,-2,-2; 2,0,-1,-2,2,-1,-2,4,0; 2,2,-2,0,0,1,-2,0,4];}
qfperfection(d)
{d=[4,2,-2,2,2,-2,-1,0;2,4,-2,0,2,-2,1,-1; -2,-2,4,-2,0,2,1,-1;
2,0,-2,4,1,0,-2,0; 2,2,0,1,4,-1,1,-2;-2,-2,2,0,-1,4,-1,-1;
-1,1,1,-2,1,-1,4,0;0,-1,-1,0,-2,-1,0,4];}
qfperfection(d)

d=[2,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1;-1,2,1,0,1,1,1,1,1,1,1,1;-1,1,2,1,1,1,1,1, 1,1,1,1;-1,0,1,2,1,1,1,1,1,1,1,1;-1,1,1,1,2,1,1,1,1,1,1,1;-1,1,1,1,1,2,1,1,1,1,1 ,1;-1,1,1,1,1,1,2,1,1,1,1,1;-1,1,1,1,1,1,1,2,1,1,1,1;-1,1,1,1,1,1,1,1,2,1,1,1;-1 ,1,1,1,1,1,1,1,1,2,1,1;-1,1,1,1,1,1,1,1,1,1,2,1;-1,1,1,1,1,1,1,1,1,1,1,2];
qfperfection(d)

d=[84,-42,42,-34,49,42,44,-5,42,-42,42,34;-42,84,-42,-8,-44,-42,-47,-20,-22,0,-17,8;42,-42,84,-34,49,42,47,-22,22,-42,22,20;-34,-8,-34,84,3,-34,-31,0,8,34,-5,-42;49,-44,49,3,98,49,49,-27,49,-27,49,-8;42,-42,42,-34,49,84,42,-8,22,-20,24,-8;44,-47,47,-31,49,42,94,20,2,-22,2,25;-5,-20,-22,0,-27,-8,20,84,-42,42,-5,-8;42,-22,22,8,49,22,2,-42,84,-42,42,9;-42,0,-42,34,-27,-20,-22,42,-42,84,-5,-28;42,-17,22,-5,49,24,2,-5,42,-5,84,1;34,8,20,-42,-8,-8,25,-8,9,-28,1,84];
qfperfection(d)

d = [11870535336,4926369655,32404766,5833735188,-260286973,1176994945,-938673930,1133212506,-1074526606,-70224083,-516302409,2824815072,-4372545965,-3541960809,-934179491,1051267712;4926369655,11870535336,-1490432686,-875900356,3641011352,-133471097,5248732172,5339909303,1977366972,2112029217,1618397291,1453763043,-5074494971,3402204872,-6089917,-2536340118;32404766,-1490432686,11870535336,123881942,1472835948,538053943,-2072520281,-2111014772,-243328180,66329388,-1668343637,5366171257,-1644082716,1999937160,1862466413,-2684624269;5833735188,-875900356,123881942,11870535336,-4482992193,724356870,-2581885607,-1123344860,-5909559285,-374057682,-1737269060,1373350629,-685882364,-2860185796,1915679243,-2582189975;-260286973,3641011352,1472835948,-4482992193,11870535336,-3382162923,-2727082036,-172926336,3957014148,4123782659,-869026456,-712184755,1975235830,598346444,-803583682,764543726;1176994945,-133471097,538053943,724356870,-3382162923,11870535336,4149099372,-1345152733,3238996158,-1859449765,788927568,627981303,-1997619722,-5100674624,1082079081,-4600113518;-938673930,5248732172,-2072520281,-2581885607,-2727082036,4149099372,11870535336,2778219046,565855490,-4509773947,2630869581,161812815,-2518706476,2620761340,1350174537,-1070307221;1133212506,5339909303,-2111014772,-1123344860,-172926336,-1345152733,2778219046,11870535336,1405373352,-94842121,5935267668,1644886404,-4169157373,1191448802,400673054,-137185759;-1074526606,1977366972,-243328180,-5909559285,3957014148,3238996158,565855490,1405373352,11870535336,-1017421319,-2747041871,-2019274686,1090295757,2591545854,433617674,63706423;-70224083,2112029217,66329388,-374057682,4123782659,-1859449765,-4509773947,-94842121,-1017421319,11870535336,-570490848,1731611845,-2658074571,-1297231573,-350469672,-40728837;-516302409,1618397291,-1668343637,-1737269060,-869026456,788927568,2630869581,5935267668,-2747041871,-570490848,11870535336,2791532769,26571128,-1302311714,1214830887,1283425367;2824815072,1453763043,5366171257,1373350629,-712184755,627981303,161812815,1644886404,-2019274686,1731611845,2791532769,11870535336,-3163139204,110178163,-49759695,-1512817003;-4372545965,-5074494971,-1644082716,-685882364,1975235830,-1997619722,-2518706476,-4169157373,1090295757,-2658074571,26571128,-3163139204,11870535336,-55032693,-2820423865,4651789746;-3541960809,3402204872,1999937160,-2860185796,598346444,-5100674624,2620761340,1191448802,2591545854,-1297231573,-1302311714,110178163,-55032693,11870535336,5683626972,-2169747194;-934179491,-6089917,1862466413,1915679243,-803583682,1082079081,1350174537,400673054,433617674,-350469672,1214830887,-49759695,-2820423865,5683626972,11870535336,-5697137302;1051267712,-2536340118,-2684624269,-2582189975,764543726,-4600113518,-1070307221,-137185759,63706423,-40728837,1283425367,-1512817003,4651789746,-2169747194,-5697137302,11870535336];
qfperfection(d)
"""
import unittest
from cypari2 import Pari, PariError

pari = Pari()


class TestMinim(unittest.TestCase):
    def test_minim(self):
        d = ('[4,2,-2,-2,2,1,-2,2,2; 2,4,-2,0,0,0,-1,0,2; -2,-2,4,2,-2,1,1,-1,-2;-2,0,2,4,-3,1,0,-2,0; 2,0,-2,-3' 
        ',4,-1,0,2,0; 1,0,1,1,-1,4,0,-1,1;-2,-1,1,0,0,0,4,-2,-2; 2,0,-1,-2,2,-1,-2,4,0; 2,2,-2,0,0,1,-2,0,4]');
        self.assertEquals(pari.qfperfection(d), '1')

        d = ('[4,2,-2,2,2,-2,-1,0;2,4,-2,0,2,-2,1,-1; -2,-2,4,-2,0,2,1,-1;'
        '2,0,-2,4,1,0,-2,0; 2,2,0,1,4,-1,1,-2;-2,-2,2,0,-1,4,-1,-1;'
        '-1,1,1,-2,1,-1,4,0;0,-1,-1,0,-2,-1,0,4]')
        self.assertEquals(pari.qfperfection(d), '1')

        d = ('[2,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1;-1,2,1,0,1,1,1,1,1,1,1,1;-1,1,2,1,1,1,1,1, 1,1,1,1;'
          '-1,0,1,2,1,1,1,1,1,1,1,1;-1,1,1,1,2,1,1,1,1,1,1,1;-1,1,1,1,1,2,1,1,1,1,1 ,1;-1,1,1,1,1,'
          '1,2,1,1,1,1,1;-1,1,1,1,1,1,1,2,1,1,1,1;-1,1,1,1,1,1,1,1,2,1,1,1;-1 ,1,1,1,1,1,1,1,1,2,1'
          ',1;-1,1,1,1,1,1,1,1,1,1,2,1;-1,1,1,1,1,1,1,1,1,1,1,2];')
        self.assertEquals(pari.qfperfection(d), '78')

        d = ('[84,-42,42,-34,49,42,44,-5,42,-42,42,34;-42,84,-42,-8,-44,-42,-47,-20,-22,0,-17,8;'
        '42,-42,84,-34,49,42,47,-22,22,-42,22,20;-34,-8,-34,84,3,-34,-31,0,8,34,-5,-42;49,-44,'
        '49,3,98,49,49,-27,49,-27,49,-8;42,-42,42,-34,49,84,42,-8,22,-20,24,-8;44,-47,47,-31,4'
        '9,42,94,20,2,-22,2,25;-5,-20,-22,0,-27,-8,20,84,-42,42,-5,-8;42,-22,22,8,49,22,2,-42,'
        '84,-42,42,9;-42,0,-42,34,-27,-20,-22,42,-42,84,-5,-28;42,-17,22,-5,49,24,2,-5,42,-5,8'
        '4,1;34,8,20,-42,-8,-8,25,-8,9,-28,1,84];')
        self.assertEquals(pari.qfperfection(d), '77')

        d = ('[11870535336,4926369655,32404766,5833735188,-260286973,1176994945,-938673930,113'
             '3212506,-1074526606,-70224083,-516302409,2824815072,-4372545965,-3541960809,-934'
             '179491,1051267712;4926369655,11870535336,-1490432686,-875900356,3641011352,-1334'
             '71097,5248732172,5339909303,1977366972,2112029217,1618397291,1453763043,-5074494'
             '971,3402204872,-6089917,-2536340118;32404766,-1490432686,11870535336,123881942,1'
             '472835948,538053943,-2072520281,-2111014772,-243328180,66329388,-1668343637,5366'
             '171257,-1644082716,1999937160,1862466413,-2684624269;5833735188,-875900356,12388'
             '1942,11870535336,-4482992193,724356870,-2581885607,-1123344860,-5909559285,-3740'
             '57682,-1737269060,1373350629,-685882364,-2860185796,1915679243,-2582189975;-2602'
             '86973,3641011352,1472835948,-4482992193,11870535336,-3382162923,-2727082036,-172'
             '926336,3957014148,4123782659,-869026456,-712184755,1975235830,598346444,-8035836'
             '82,764543726;1176994945,-133471097,538053943,724356870,-3382162923,11870535336,4'
             '149099372,-1345152733,3238996158,-1859449765,788927568,627981303,-1997619722,-51'
             '00674624,1082079081,-4600113518;-938673930,5248732172,-2072520281,-2581885607,-2'
             '727082036,4149099372,11870535336,2778219046,565855490,-4509773947,2630869581,161'
             '812815,-2518706476,2620761340,1350174537,-1070307221;1133212506,5339909303,-2111'
             '014772,-1123344860,-172926336,-1345152733,2778219046,11870535336,1405373352,-948'
             '42121,5935267668,1644886404,-4169157373,1191448802,400673054,-137185759;-1074526'
             '606,1977366972,-243328180,-5909559285,3957014148,3238996158,565855490,1405373352'
             ',11870535336,-1017421319,-2747041871,-2019274686,1090295757,2591545854,433617674'
             ',63706423;-70224083,2112029217,66329388,-374057682,4123782659,-1859449765,-45097'
             '73947,-94842121,-1017421319,11870535336,-570490848,1731611845,-2658074571,-12972'
             '31573,-350469672,-40728837;-516302409,1618397291,-1668343637,-1737269060,-869026'
             '456,788927568,2630869581,5935267668,-2747041871,-570490848,11870535336,279153276'
             '9,26571128,-1302311714,1214830887,1283425367;2824815072,1453763043,5366171257,13'
             '73350629,-712184755,627981303,161812815,1644886404,-2019274686,1731611845,279153'
             '2769,11870535336,-3163139204,110178163,-49759695,-1512817003;-4372545965,-507449'
             '4971,-1644082716,-685882364,1975235830,-1997619722,-2518706476,-4169157373,10902'
             '95757,-2658074571,26571128,-3163139204,11870535336,-55032693,-2820423865,4651789'
             '746;-3541960809,3402204872,1999937160,-2860185796,598346444,-5100674624,26207613'
             '40,1191448802,2591545854,-1297231573,-1302311714,110178163,-55032693,11870535336'
             ',5683626972,-2169747194;-934179491,-6089917,1862466413,1915679243,-803583682,108'
             '2079081,1350174537,400673054,433617674,-350469672,1214830887,-49759695,-28204238'
             '65,5683626972,11870535336,-5697137302;1051267712,-2536340118,-2684624269,-258218'
             '9975,764543726,-4600113518,-1070307221,-137185759,63706423,-40728837,1283425367,'
             '-1512817003,4651789746,-2169747194,-5697137302,11870535336];')
        self.assertEquals(pari.qfperfection(d), '136')

"""**** Original expected results ****

1
1
78
77
136

"""
