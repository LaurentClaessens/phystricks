from phystricks import *

"""
This file contains only doctests with output too long to be included in the code itself.

sage: P=Point(1,1)
sage: P.length()
sqrt(2)

sage: var('x,y')
(x, y)
sage: f(x,y)=sin(x)
sage: curve=ImplicitCurve(f==1/2,(x,-pi,pi),(y,-pi,pi))
sage: curve.pstricks_code()
'\\pscurve[linestyle=solid,linecolor=blue](0.523636811204084,-3.14159265358979)(0.523636811204084,-3.09942362468255)(0.523636811204084,-3.05725459577530)(0.523636811204084,-3.01508556686806)(0.523636811204084,-2.97291653796081)(0.523636811204084,-2.93074750905357)(0.523636811204084,-2.88857848014632)(0.523636811204084,-2.84640945123907)(0.523636811204084,-2.80424042233183)(0.523636811204084,-2.76207139342458)(0.523636811204084,-2.71990236451734)(0.523636811204084,-2.67773333561009)(0.523636811204084,-2.63556430670285)(0.523636811204084,-2.59339527779560)(0.523636811204084,-2.55122624888836)(0.523636811204084,-2.50905721998111)(0.523636811204084,-2.46688819107386)(0.523636811204084,-2.42471916216662)(0.523636811204084,-2.38255013325937)(0.523636811204084,-2.34038110435213)(0.523636811204084,-2.29821207544488)(0.523636811204084,-2.25604304653764)(0.523636811204084,-2.21387401763039)(0.523636811204084,-2.17170498872315)(0.523636811204084,-2.12953595981590)(0.523636811204084,-2.08736693090865)(0.523636811204084,-2.04519790200141)(0.523636811204084,-2.00302887309416)(0.523636811204084,-1.96085984418692)(0.523636811204084,-1.91869081527967)(0.523636811204084,-1.87652178637243)(0.523636811204084,-1.83435275746518)(0.523636811204084,-1.79218372855794)(0.523636811204084,-1.75001469965069)(0.523636811204084,-1.70784567074344)(0.523636811204084,-1.66567664183620)(0.523636811204084,-1.62350761292895)(0.523636811204084,-1.58133858402171)(0.523636811204084,-1.53916955511446)(0.523636811204084,-1.49700052620722)(0.523636811204084,-1.45483149729997)(0.523636811204084,-1.41266246839273)(0.523636811204084,-1.37049343948548)(0.523636811204084,-1.32832441057823)(0.523636811204084,-1.28615538167099)(0.523636811204084,-1.24398635276374)(0.523636811204084,-1.20181732385650)(0.523636811204084,-1.15964829494925)(0.523636811204084,-1.11747926604201)(0.523636811204084,-1.07531023713476)(0.523636811204084,-1.03314120822752)(0.523636811204084,-0.990972179320270)(0.523636811204084,-0.948803150413025)(0.523636811204084,-0.906634121505779)(0.523636811204084,-0.864465092598534)(0.523636811204084,-0.822296063691288)(0.523636811204084,-0.780127034784043)(0.523636811204084,-0.737958005876797)(0.523636811204084,-0.695788976969551)(0.523636811204084,-0.653619948062306)(0.523636811204084,-0.611450919155060)(0.523636811204084,-0.569281890247815)(0.523636811204084,-0.527112861340569)(0.523636811204084,-0.484943832433324)(0.523636811204084,-0.442774803526078)(0.523636811204084,-0.400605774618833)(0.523636811204084,-0.358436745711587)(0.523636811204084,-0.316267716804342)(0.523636811204084,-0.274098687897096)(0.523636811204084,-0.231929658989850)(0.523636811204084,-0.189760630082605)(0.523636811204084,-0.147591601175359)(0.523636811204084,-0.105422572268114)(0.523636811204084,-0.0632535433608683)(0.523636811204084,-0.0210845144536225)(0.523636811204084,0.0210845144536229)(0.523636811204084,0.0632535433608683)(0.523636811204084,0.105422572268114)(0.523636811204084,0.147591601175360)(0.523636811204084,0.189760630082605)(0.523636811204084,0.231929658989851)(0.523636811204084,0.274098687897096)(0.523636811204084,0.316267716804342)(0.523636811204084,0.358436745711587)(0.523636811204084,0.400605774618833)(0.523636811204084,0.442774803526079)(0.523636811204084,0.484943832433324)(0.523636811204084,0.527112861340569)(0.523636811204084,0.569281890247815)(0.523636811204084,0.611450919155061)(0.523636811204084,0.653619948062306)(0.523636811204084,0.695788976969552)(0.523636811204084,0.737958005876797)(0.523636811204084,0.780127034784043)(0.523636811204084,0.822296063691288)(0.523636811204084,0.864465092598534)(0.523636811204084,0.906634121505779)(0.523636811204084,0.948803150413025)(0.523636811204084,0.990972179320271)(0.523636811204084,1.03314120822752)(0.523636811204084,1.07531023713476)(0.523636811204084,1.11747926604201)(0.523636811204084,1.15964829494925)(0.523636811204084,1.20181732385650)(0.523636811204084,1.24398635276374)(0.523636811204084,1.28615538167099)(0.523636811204084,1.32832441057823)(0.523636811204084,1.37049343948548)(0.523636811204084,1.41266246839273)(0.523636811204084,1.45483149729997)(0.523636811204084,1.49700052620722)(0.523636811204084,1.53916955511446)(0.523636811204084,1.58133858402171)(0.523636811204084,1.62350761292895)(0.523636811204084,1.66567664183620)(0.523636811204084,1.70784567074344)(0.523636811204084,1.75001469965069)(0.523636811204084,1.79218372855794)(0.523636811204084,1.83435275746518)(0.523636811204084,1.87652178637243)(0.523636811204084,1.91869081527967)(0.523636811204084,1.96085984418692)(0.523636811204084,2.00302887309416)(0.523636811204084,2.04519790200141)(0.523636811204084,2.08736693090865)(0.523636811204084,2.12953595981590)(0.523636811204084,2.17170498872315)(0.523636811204084,2.21387401763039)(0.523636811204084,2.25604304653764)(0.523636811204084,2.29821207544488)(0.523636811204084,2.34038110435213)(0.523636811204084,2.38255013325937)(0.523636811204084,2.42471916216662)(0.523636811204084,2.46688819107386)(0.523636811204084,2.50905721998111)(0.523636811204084,2.55122624888836)(0.523636811204084,2.59339527779560)(0.523636811204084,2.63556430670285)(0.523636811204084,2.67773333561009)(0.523636811204084,2.71990236451734)(0.523636811204084,2.76207139342458)(0.523636811204084,2.80424042233183)(0.523636811204084,2.84640945123907)(0.523636811204084,2.88857848014632)(0.523636811204084,2.93074750905357)(0.523636811204084,2.97291653796081)(0.523636811204084,3.01508556686806)(0.523636811204084,3.05725459577530)(0.523636811204084,3.09942362468255)(0.523636811204084,3.14159265358979)\n\\pscurve[linestyle=solid,linecolor=blue](2.61786834431489,-3.14159265358979)(2.61786834431489,-3.09942362468255)(2.61786834431489,-3.05725459577530)(2.61786834431489,-3.01508556686806)(2.61786834431489,-2.97291653796081)(2.61786834431489,-2.93074750905357)(2.61786834431489,-2.88857848014632)(2.61786834431489,-2.84640945123907)(2.61786834431489,-2.80424042233183)(2.61786834431489,-2.76207139342458)(2.61786834431489,-2.71990236451734)(2.61786834431489,-2.67773333561009)(2.61786834431489,-2.63556430670285)(2.61786834431489,-2.59339527779560)(2.61786834431489,-2.55122624888836)(2.61786834431489,-2.50905721998111)(2.61786834431489,-2.46688819107386)(2.61786834431489,-2.42471916216662)(2.61786834431489,-2.38255013325937)(2.61786834431489,-2.34038110435213)(2.61786834431489,-2.29821207544488)(2.61786834431489,-2.25604304653764)(2.61786834431489,-2.21387401763039)(2.61786834431489,-2.17170498872315)(2.61786834431489,-2.12953595981590)(2.61786834431489,-2.08736693090865)(2.61786834431489,-2.04519790200141)(2.61786834431489,-2.00302887309416)(2.61786834431489,-1.96085984418692)(2.61786834431489,-1.91869081527967)(2.61786834431489,-1.87652178637243)(2.61786834431489,-1.83435275746518)(2.61786834431489,-1.79218372855794)(2.61786834431489,-1.75001469965069)(2.61786834431489,-1.70784567074344)(2.61786834431489,-1.66567664183620)(2.61786834431489,-1.62350761292895)(2.61786834431489,-1.58133858402171)(2.61786834431489,-1.53916955511446)(2.61786834431489,-1.49700052620722)(2.61786834431489,-1.45483149729997)(2.61786834431489,-1.41266246839273)(2.61786834431489,-1.37049343948548)(2.61786834431489,-1.32832441057823)(2.61786834431489,-1.28615538167099)(2.61786834431489,-1.24398635276374)(2.61786834431489,-1.20181732385650)(2.61786834431489,-1.15964829494925)(2.61786834431489,-1.11747926604201)(2.61786834431489,-1.07531023713476)(2.61786834431489,-1.03314120822752)(2.61786834431489,-0.990972179320270)(2.61786834431489,-0.948803150413025)(2.61786834431489,-0.906634121505779)(2.61786834431489,-0.864465092598534)(2.61786834431489,-0.822296063691288)(2.61786834431489,-0.780127034784043)(2.61786834431489,-0.737958005876797)(2.61786834431489,-0.695788976969551)(2.61786834431489,-0.653619948062306)(2.61786834431489,-0.611450919155060)(2.61786834431489,-0.569281890247815)(2.61786834431489,-0.527112861340569)(2.61786834431489,-0.484943832433324)(2.61786834431489,-0.442774803526078)(2.61786834431489,-0.400605774618833)(2.61786834431489,-0.358436745711587)(2.61786834431489,-0.316267716804342)(2.61786834431489,-0.274098687897096)(2.61786834431489,-0.231929658989850)(2.61786834431489,-0.189760630082605)(2.61786834431489,-0.147591601175359)(2.61786834431489,-0.105422572268114)(2.61786834431489,-0.0632535433608683)(2.61786834431489,-0.0210845144536225)(2.61786834431489,0.0210845144536229)(2.61786834431489,0.0632535433608683)(2.61786834431489,0.105422572268114)(2.61786834431489,0.147591601175360)(2.61786834431489,0.189760630082605)(2.61786834431489,0.231929658989851)(2.61786834431489,0.274098687897096)(2.61786834431489,0.316267716804342)(2.61786834431489,0.358436745711587)(2.61786834431489,0.400605774618833)(2.61786834431489,0.442774803526079)(2.61786834431489,0.484943832433324)(2.61786834431489,0.527112861340569)(2.61786834431489,0.569281890247815)(2.61786834431489,0.611450919155061)(2.61786834431489,0.653619948062306)(2.61786834431489,0.695788976969552)(2.61786834431489,0.737958005876797)(2.61786834431489,0.780127034784043)(2.61786834431489,0.822296063691288)(2.61786834431489,0.864465092598534)(2.61786834431489,0.906634121505779)(2.61786834431489,0.948803150413025)(2.61786834431489,0.990972179320271)(2.61786834431489,1.03314120822752)(2.61786834431489,1.07531023713476)(2.61786834431489,1.11747926604201)(2.61786834431489,1.15964829494925)(2.61786834431489,1.20181732385650)(2.61786834431489,1.24398635276374)(2.61786834431489,1.28615538167099)(2.61786834431489,1.32832441057823)(2.61786834431489,1.37049343948548)(2.61786834431489,1.41266246839273)(2.61786834431489,1.45483149729997)(2.61786834431489,1.49700052620722)(2.61786834431489,1.53916955511446)(2.61786834431489,1.58133858402171)(2.61786834431489,1.62350761292895)(2.61786834431489,1.66567664183620)(2.61786834431489,1.70784567074344)(2.61786834431489,1.75001469965069)(2.61786834431489,1.79218372855794)(2.61786834431489,1.83435275746518)(2.61786834431489,1.87652178637243)(2.61786834431489,1.91869081527967)(2.61786834431489,1.96085984418692)(2.61786834431489,2.00302887309416)(2.61786834431489,2.04519790200141)(2.61786834431489,2.08736693090865)(2.61786834431489,2.12953595981590)(2.61786834431489,2.17170498872315)(2.61786834431489,2.21387401763039)(2.61786834431489,2.25604304653764)(2.61786834431489,2.29821207544488)(2.61786834431489,2.34038110435213)(2.61786834431489,2.38255013325937)(2.61786834431489,2.42471916216662)(2.61786834431489,2.46688819107386)(2.61786834431489,2.50905721998111)(2.61786834431489,2.55122624888836)(2.61786834431489,2.59339527779560)(2.61786834431489,2.63556430670285)(2.61786834431489,2.67773333561009)(2.61786834431489,2.71990236451734)(2.61786834431489,2.76207139342458)(2.61786834431489,2.80424042233183)(2.61786834431489,2.84640945123907)(2.61786834431489,2.88857848014632)(2.61786834431489,2.93074750905357)(2.61786834431489,2.97291653796081)(2.61786834431489,3.01508556686806)(2.61786834431489,3.05725459577530)(2.61786834431489,3.09942362468255)(2.61786834431489,3.14159265358979)\n\\pscurve[linestyle=solid,linecolor=blue](0.523636811204084,-3.14159265358979)(0.523636811204084,-3.09942362468255)(0.523636811204084,-3.05725459577530)(0.523636811204084,-3.01508556686806)(0.523636811204084,-2.97291653796081)(0.523636811204084,-2.93074750905357)(0.523636811204084,-2.88857848014632)(0.523636811204084,-2.84640945123907)(0.523636811204084,-2.80424042233183)(0.523636811204084,-2.76207139342458)(0.523636811204084,-2.71990236451734)(0.523636811204084,-2.67773333561009)(0.523636811204084,-2.63556430670285)(0.523636811204084,-2.59339527779560)(0.523636811204084,-2.55122624888836)(0.523636811204084,-2.50905721998111)(0.523636811204084,-2.46688819107386)(0.523636811204084,-2.42471916216662)(0.523636811204084,-2.38255013325937)(0.523636811204084,-2.34038110435213)(0.523636811204084,-2.29821207544488)(0.523636811204084,-2.25604304653764)(0.523636811204084,-2.21387401763039)(0.523636811204084,-2.17170498872315)(0.523636811204084,-2.12953595981590)(0.523636811204084,-2.08736693090865)(0.523636811204084,-2.04519790200141)(0.523636811204084,-2.00302887309416)(0.523636811204084,-1.96085984418692)(0.523636811204084,-1.91869081527967)(0.523636811204084,-1.87652178637243)(0.523636811204084,-1.83435275746518)(0.523636811204084,-1.79218372855794)(0.523636811204084,-1.75001469965069)(0.523636811204084,-1.70784567074344)(0.523636811204084,-1.66567664183620)(0.523636811204084,-1.62350761292895)(0.523636811204084,-1.58133858402171)(0.523636811204084,-1.53916955511446)(0.523636811204084,-1.49700052620722)(0.523636811204084,-1.45483149729997)(0.523636811204084,-1.41266246839273)(0.523636811204084,-1.37049343948548)(0.523636811204084,-1.32832441057823)(0.523636811204084,-1.28615538167099)(0.523636811204084,-1.24398635276374)(0.523636811204084,-1.20181732385650)(0.523636811204084,-1.15964829494925)(0.523636811204084,-1.11747926604201)(0.523636811204084,-1.07531023713476)(0.523636811204084,-1.03314120822752)(0.523636811204084,-0.990972179320270)(0.523636811204084,-0.948803150413025)(0.523636811204084,-0.906634121505779)(0.523636811204084,-0.864465092598534)(0.523636811204084,-0.822296063691288)(0.523636811204084,-0.780127034784043)(0.523636811204084,-0.737958005876797)(0.523636811204084,-0.695788976969551)(0.523636811204084,-0.653619948062306)(0.523636811204084,-0.611450919155060)(0.523636811204084,-0.569281890247815)(0.523636811204084,-0.527112861340569)(0.523636811204084,-0.484943832433324)(0.523636811204084,-0.442774803526078)(0.523636811204084,-0.400605774618833)(0.523636811204084,-0.358436745711587)(0.523636811204084,-0.316267716804342)(0.523636811204084,-0.274098687897096)(0.523636811204084,-0.231929658989850)(0.523636811204084,-0.189760630082605)(0.523636811204084,-0.147591601175359)(0.523636811204084,-0.105422572268114)(0.523636811204084,-0.0632535433608683)(0.523636811204084,-0.0210845144536225)(0.523636811204084,0.0210845144536229)(0.523636811204084,0.0632535433608683)(0.523636811204084,0.105422572268114)(0.523636811204084,0.147591601175360)(0.523636811204084,0.189760630082605)(0.523636811204084,0.231929658989851)(0.523636811204084,0.274098687897096)(0.523636811204084,0.316267716804342)(0.523636811204084,0.358436745711587)(0.523636811204084,0.400605774618833)(0.523636811204084,0.442774803526079)(0.523636811204084,0.484943832433324)(0.523636811204084,0.527112861340569)(0.523636811204084,0.569281890247815)(0.523636811204084,0.611450919155061)(0.523636811204084,0.653619948062306)(0.523636811204084,0.695788976969552)(0.523636811204084,0.737958005876797)(0.523636811204084,0.780127034784043)(0.523636811204084,0.822296063691288)(0.523636811204084,0.864465092598534)(0.523636811204084,0.906634121505779)(0.523636811204084,0.948803150413025)(0.523636811204084,0.990972179320271)(0.523636811204084,1.03314120822752)(0.523636811204084,1.07531023713476)(0.523636811204084,1.11747926604201)(0.523636811204084,1.15964829494925)(0.523636811204084,1.20181732385650)(0.523636811204084,1.24398635276374)(0.523636811204084,1.28615538167099)(0.523636811204084,1.32832441057823)(0.523636811204084,1.37049343948548)(0.523636811204084,1.41266246839273)(0.523636811204084,1.45483149729997)(0.523636811204084,1.49700052620722)(0.523636811204084,1.53916955511446)(0.523636811204084,1.58133858402171)(0.523636811204084,1.62350761292895)(0.523636811204084,1.66567664183620)(0.523636811204084,1.70784567074344)(0.523636811204084,1.75001469965069)(0.523636811204084,1.79218372855794)(0.523636811204084,1.83435275746518)(0.523636811204084,1.87652178637243)(0.523636811204084,1.91869081527967)(0.523636811204084,1.96085984418692)(0.523636811204084,2.00302887309416)(0.523636811204084,2.04519790200141)(0.523636811204084,2.08736693090865)(0.523636811204084,2.12953595981590)(0.523636811204084,2.17170498872315)(0.523636811204084,2.21387401763039)(0.523636811204084,2.25604304653764)(0.523636811204084,2.29821207544488)(0.523636811204084,2.34038110435213)(0.523636811204084,2.38255013325937)(0.523636811204084,2.42471916216662)(0.523636811204084,2.46688819107386)(0.523636811204084,2.50905721998111)(0.523636811204084,2.55122624888836)(0.523636811204084,2.59339527779560)(0.523636811204084,2.63556430670285)(0.523636811204084,2.67773333561009)(0.523636811204084,2.71990236451734)(0.523636811204084,2.76207139342458)(0.523636811204084,2.80424042233183)(0.523636811204084,2.84640945123907)(0.523636811204084,2.88857848014632)(0.523636811204084,2.93074750905357)(0.523636811204084,2.97291653796081)(0.523636811204084,3.01508556686806)(0.523636811204084,3.05725459577530)(0.523636811204084,3.09942362468255)(0.523636811204084,3.14159265358979)\n\\pscurve[linestyle=solid,linecolor=blue](2.61786834431489,-3.14159265358979)(2.61786834431489,-3.09942362468255)(2.61786834431489,-3.05725459577530)(2.61786834431489,-3.01508556686806)(2.61786834431489,-2.97291653796081)(2.61786834431489,-2.93074750905357)(2.61786834431489,-2.88857848014632)(2.61786834431489,-2.84640945123907)(2.61786834431489,-2.80424042233183)(2.61786834431489,-2.76207139342458)(2.61786834431489,-2.71990236451734)(2.61786834431489,-2.67773333561009)(2.61786834431489,-2.63556430670285)(2.61786834431489,-2.59339527779560)(2.61786834431489,-2.55122624888836)(2.61786834431489,-2.50905721998111)(2.61786834431489,-2.46688819107386)(2.61786834431489,-2.42471916216662)(2.61786834431489,-2.38255013325937)(2.61786834431489,-2.34038110435213)(2.61786834431489,-2.29821207544488)(2.61786834431489,-2.25604304653764)(2.61786834431489,-2.21387401763039)(2.61786834431489,-2.17170498872315)(2.61786834431489,-2.12953595981590)(2.61786834431489,-2.08736693090865)(2.61786834431489,-2.04519790200141)(2.61786834431489,-2.00302887309416)(2.61786834431489,-1.96085984418692)(2.61786834431489,-1.91869081527967)(2.61786834431489,-1.87652178637243)(2.61786834431489,-1.83435275746518)(2.61786834431489,-1.79218372855794)(2.61786834431489,-1.75001469965069)(2.61786834431489,-1.70784567074344)(2.61786834431489,-1.66567664183620)(2.61786834431489,-1.62350761292895)(2.61786834431489,-1.58133858402171)(2.61786834431489,-1.53916955511446)(2.61786834431489,-1.49700052620722)(2.61786834431489,-1.45483149729997)(2.61786834431489,-1.41266246839273)(2.61786834431489,-1.37049343948548)(2.61786834431489,-1.32832441057823)(2.61786834431489,-1.28615538167099)(2.61786834431489,-1.24398635276374)(2.61786834431489,-1.20181732385650)(2.61786834431489,-1.15964829494925)(2.61786834431489,-1.11747926604201)(2.61786834431489,-1.07531023713476)(2.61786834431489,-1.03314120822752)(2.61786834431489,-0.990972179320270)(2.61786834431489,-0.948803150413025)(2.61786834431489,-0.906634121505779)(2.61786834431489,-0.864465092598534)(2.61786834431489,-0.822296063691288)(2.61786834431489,-0.780127034784043)(2.61786834431489,-0.737958005876797)(2.61786834431489,-0.695788976969551)(2.61786834431489,-0.653619948062306)(2.61786834431489,-0.611450919155060)(2.61786834431489,-0.569281890247815)(2.61786834431489,-0.527112861340569)(2.61786834431489,-0.484943832433324)(2.61786834431489,-0.442774803526078)(2.61786834431489,-0.400605774618833)(2.61786834431489,-0.358436745711587)(2.61786834431489,-0.316267716804342)(2.61786834431489,-0.274098687897096)(2.61786834431489,-0.231929658989850)(2.61786834431489,-0.189760630082605)(2.61786834431489,-0.147591601175359)(2.61786834431489,-0.105422572268114)(2.61786834431489,-0.0632535433608683)(2.61786834431489,-0.0210845144536225)(2.61786834431489,0.0210845144536229)(2.61786834431489,0.0632535433608683)(2.61786834431489,0.105422572268114)(2.61786834431489,0.147591601175360)(2.61786834431489,0.189760630082605)(2.61786834431489,0.231929658989851)(2.61786834431489,0.274098687897096)(2.61786834431489,0.316267716804342)(2.61786834431489,0.358436745711587)(2.61786834431489,0.400605774618833)(2.61786834431489,0.442774803526079)(2.61786834431489,0.484943832433324)(2.61786834431489,0.527112861340569)(2.61786834431489,0.569281890247815)(2.61786834431489,0.611450919155061)(2.61786834431489,0.653619948062306)(2.61786834431489,0.695788976969552)(2.61786834431489,0.737958005876797)(2.61786834431489,0.780127034784043)(2.61786834431489,0.822296063691288)(2.61786834431489,0.864465092598534)(2.61786834431489,0.906634121505779)(2.61786834431489,0.948803150413025)(2.61786834431489,0.990972179320271)(2.61786834431489,1.03314120822752)(2.61786834431489,1.07531023713476)(2.61786834431489,1.11747926604201)(2.61786834431489,1.15964829494925)(2.61786834431489,1.20181732385650)(2.61786834431489,1.24398635276374)(2.61786834431489,1.28615538167099)(2.61786834431489,1.32832441057823)(2.61786834431489,1.37049343948548)(2.61786834431489,1.41266246839273)(2.61786834431489,1.45483149729997)(2.61786834431489,1.49700052620722)(2.61786834431489,1.53916955511446)(2.61786834431489,1.58133858402171)(2.61786834431489,1.62350761292895)(2.61786834431489,1.66567664183620)(2.61786834431489,1.70784567074344)(2.61786834431489,1.75001469965069)(2.61786834431489,1.79218372855794)(2.61786834431489,1.83435275746518)(2.61786834431489,1.87652178637243)(2.61786834431489,1.91869081527967)(2.61786834431489,1.96085984418692)(2.61786834431489,2.00302887309416)(2.61786834431489,2.04519790200141)(2.61786834431489,2.08736693090865)(2.61786834431489,2.12953595981590)(2.61786834431489,2.17170498872315)(2.61786834431489,2.21387401763039)(2.61786834431489,2.25604304653764)(2.61786834431489,2.29821207544488)(2.61786834431489,2.34038110435213)(2.61786834431489,2.38255013325937)(2.61786834431489,2.42471916216662)(2.61786834431489,2.46688819107386)(2.61786834431489,2.50905721998111)(2.61786834431489,2.55122624888836)(2.61786834431489,2.59339527779560)(2.61786834431489,2.63556430670285)(2.61786834431489,2.67773333561009)(2.61786834431489,2.71990236451734)(2.61786834431489,2.76207139342458)(2.61786834431489,2.80424042233183)(2.61786834431489,2.84640945123907)(2.61786834431489,2.88857848014632)(2.61786834431489,2.93074750905357)(2.61786834431489,2.97291653796081)(2.61786834431489,3.01508556686806)(2.61786834431489,3.05725459577530)(2.61786834431489,3.09942362468255)(2.61786834431489,3.14159265358979)'

"""



