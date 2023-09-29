# Code#LikeABosch

## Softwaredevelopmentchallenge

Yourtaskfortheupcoming 24 hourswillincludeimplementingasolutionforvehicle
collisionavoidanceaswellthinkinglikeaninnovatoranddeliveringthenextgeneration
ofdriverassistancesystems.Joinusonthisexcitingchallenge!

## Whoweare?

Boschisoneofthemarketandtechnologyleadersintheautomotiveindustry,innearly
allfieldsofvehiclesandtransportationtoourpartners.Weprovidesoftware,hardware,
and system solutions in the field of vehicle safety, vehicle dynamics, and driver
assistance.Throughthecombinationofsystemsbasedoncameras,radars,ultrasonic
sensors,electric power steering, andactiveorpassivesafetysystems.We notonly
makedrivingsaferandmorecomfortabletoday,butwearealsobuildingthebasisfor
theautonomousdrivingoftomorrow.

## Background

Driverassistancesystemsarecontinuouslybeingdevelopedtosupportthedriverand
otherroadparticipantsmoreandmore.Thesesystemsconsistof 4 mainlayers.

```
● SensingLayer:usingcamera,radar,andsometimeslidarsensors
● Perceptionlayer:detectionandclassificationoftheobjectsaroundthevehicle
● Situation layer: object tracking and estimating the behaviour of the car’s
environment.
● Function layer: based on all theabove make decision howourvehicleshall
behave
```
Researchanddevelopmentareheavilyandparallellyongoinginalllayerstoprovide
moreadvancedsafetyandcomforttofuturevehicles,andofcoursetostrengthenand
developthecompany’smarketposition.Nowweareinvitingyoutojointhesetasksin
the’Perceptionlayer’,’Situationlayer’andthe’Functionlayer’.

Fornow,mostofthevehicles(from07.2024allofthem)havetohaveafunctionwhich


iscalledAutomaticEmergencyBrake(AEB).Acar,whichhasAEBcanavoid,ormitigate
collisionautomatically, without anydriver intervention.Thereareseveralscenarios,
whicharehandledbyAEB. Thiscanworkwithonesensor(1radar,or 1 videocamera),
orinafusionmode,wherethecameraandtheradarprovidefusedobjects(bothof
themseetheobject),whichwillbeprocessedbyPerception.Thatlayeridentifiesthe
object,whatitis(vehicle,pedestrian(adult,child),motorcyclist). Afterthat,itdecidesif
thetargetisrelevantforthesystem,ornot.Afterthat,theSituationlayerwillprocess
thisinformation,andevaluate,whatisthescenario(turning,longitudinal,crossing).If
theidentificationhappened,they decideif theFunctionlayershouldreactforthese
objectsintheevaluatedscenario,ornot.Iftheanswerisyes,thentheFunctionlayer
willstartthereaction,andtrytoavoid,oratleastmitigatethecollision.

## Challenge

Thereare 3 partstothechallenge.Itisnotmandatorytocompleteallthetasks,it’sup
toyouwhichpart,orpartsyoutarget,butpleasebeaware,ifyoudon’tdothe1stpart,
youwon’tbecapableofdoingthesecondandthethirdpartofthechallenge.Youcan
skipthesecond,and/orthethirdpart,themaingoalistobeaspreciseasyoucanin
theimplementationandinthepresentationaswell.Thechallengedetailswillbeshared
attheendofthedocumentin’Judgingcriteria’.Don’tforget,youareheretohave

```
fun, andshow yourexpert skills!We areprettysure,thechallengewillbereallya
challenge,butatthesametime,itwillbealotoffun.
```
Inthischallengethefollowingsensorwillbeused: **Frontvideocamera**

```
Inthefirstpart youhavetofilteroutalltheunnecessarytargetobjects,andfindwith
thevisualizationthecorrectscenario(thescenariosarelistedinthesecondpartofthe
challenge).Youhavetomeasurethelongitudinalandlateraldistanceoftherelevant
objectfromthevehicle,andthespeedofit.Fromthisinformationyouhavetocreate
theenvironment of the vehicle, how the object andvehicle move, anddefinethe
scenario.
Ourexpectationisthatyoucanpresent(visualize)theenvironmentofthevehicle,the
relevantobject,thevehicle’sandtargetobject’sspeed.Soallinall,allthemotionsand
thefullenvironmentandthescenarioshouldbevisualized.
Thevisualizationcanbeanything,whatyouknow,andcapableofthat.Forexample
(pythonscript,.NET,UnrealEngine,Javascriptetc..)
● Basedon theavailabledatacreateavisualizationofhowthevehicleandthe
```

```
relevantobjectmove,andthefullenvironment
● Filteroutalltheunnecessarytargetobjects,calculatethespeedofthevehicle
timestamptotimestamp,andaswellthetargetobject’sspeed,thelongitudinal
andlateraldistancefromthevehicle.
```
Youwillgetadatabase(intheformatof.csv)fromarealvehiclemeasurement,which
willcontainalltherelevantinformation(objects,speeds,distances).

```
Thesecondpart istodecideaboutthefirstparty's information,andwhatkindof
scenariohappensbasedonyourvisualization.Herearethechooseablescenarios:
● CPNCO–CartoPedestrianNearsideChildObstructed
```
Acollisioninwhichavehicletravelsforwardstowardsachildpedestriancrossingits
pathrunningfrombehindandobstructionfromthenearsideandthefrontalstructure
ofthevehicle strikesthepedestrianat50%ofthevehicle'swidthwhennobraking
actionisapplied.

```
● CPTA–CartoPedestrianTurnAdult
```
A collisionin whicha vehicle turns towardsan adult pedestrian crossing its path,
walkingacrossajunction(ineitherthesameandoppositedirectionastheVUT,before
theVUTmadetheturn)andthefrontalstructureofthevehiclestrikesthepedestrianat
50%ofthevehicle'swidthwhennobrakingactionisapplied.


```
● CPLA–CartoPedestrianLongitudinalAdult
```
Acollisioninwhichavehicletravelsforwardstowardsanadultpedestrianwalkingin
thesamedirectioninfrontofthevehiclewherethevehiclestrikesthepedestrianat
50%ofthevehicle’swidthwhennobrakingactionisapplied.

Ifyouidentifiedthescenarioyoucanmovetothethirdpartofthechallenge.

```
Thethirdandfinalpart istoimplementasolution,whichcanavoidthecollision.The
solutionistotallyuptoyou,howyouwouldliketodoit.Justsomehints:
● Signaltothetargetobjectwiththehorn
● Flashthefrontheadlightstotheobject
● Flashing/soundalarmofthepedestriancrossinglight
● Calculatethebrakedistance,andhowmuchdecelerationneededtoavoidthe
collision.Forthat,herearesomehelp:
```

BrakeDistanceCalculation

∆𝑑=𝑑 1 +𝑑 2 +𝑑 3

𝑑 1 =𝑣𝑒𝑔𝑜*𝑡𝑙𝑎𝑡+

```
𝑎𝑒𝑔𝑜
2 *𝑡𝑙𝑎𝑡
```
```
2
```
### 𝑑 2 = 𝑚𝑎𝑥 6 𝐽𝑒𝑟𝑘 *𝑡 23 +

```
𝑎𝑒𝑔𝑜
2 *𝑡 2
```
(^2) +𝑣
𝑒𝑔𝑜*𝑡 2
𝑑 3 =
𝑎𝑚𝑎𝑥
2 *𝑡 3
(^2) +𝑣
1 *𝑡 3
𝑡 2 =
𝑎𝑚𝑎𝑥−𝑎𝑒𝑔𝑜
𝑚𝑎𝑥𝐽𝑒𝑟𝑘
𝑡 3 =
∆𝑣 2
𝑎𝑚𝑎𝑥
∆𝑣 2 = −𝑣 1
𝑣 1 =𝑣 0 + ∆𝑣 1
∆𝑣 1 = 𝑚𝑎𝑥 2 𝐽𝑒𝑟𝑘 *𝑡 22 +𝑎𝑒𝑔𝑜*𝑡 2
Hint: FormaxJerk,use− 30 𝑚/𝑠^3 ,aEgoistheacceleration/decelerationofthevehicle,
aMaxisthemaximumdeceleration.Use − 9 𝑚/𝑠^2 .vEgoisthespeedofthevehicle.
Use your creativity! Themain goal of thistask is toavoidcollisions!Butitcanbe
accepted,ifyouprovideatheoreticalsolution.

## Whatwewillprovide

```
TwokindsofdatasetswillbeusedduringtheHackathon:
★ Developmentdataset
★ Validationdataset
```

Development dataset: You will be provided a dataset that you can use for your
development.

Validationdataset:Thiswillbeavailableonlyforthementorsandjury,andforyou,
afterthefinalizationofthetasks.Checkingyoursolutionsonthisdatasetmakessure
thatyoudon’toveroptimizeyourimplementationtoyourdevelopmentdataset.

```
Thedatasetsarein.csvformat,andcontainsthefollowinginfo:
● timestamps
● objects,objectpositions,velocities
```
## Implementationandtechnology

AsweareworkingonembeddedsystemsatBosch,wemostlyuseC++,butyouarefree
touseanykindoftechnologiesandlanguagestosolvethechallengeabove.

## Judgingcriteria

**Firstpartofthechallenge:Objectfilteringandenvironment/situationbuild-up**

```
● Youcanpresentthesolutionvisually
● Onlytherelevantobjectandthevehicleareonthevisualizedpicture/video/gif
```
**Secondpartofthechallenge:Situationdecision**

```
● Youwereabletochoosewhichscenariohappenedaboutthedata
```
**Thirdpartofthechallenge:Avoidormitigatethecollision**

```
● Youwereabletoimplementasolution,whichcanavoidormitigatethecollision
withthetargetobject
● Notnecessarytoimplementa visualsolution,it’senoughtobeabletoshare
yourthoughtsandprovetheidea
```
**Innovativeness**

**Feasibility**

```
● Wewouldliketoseeawalkthroughstepbystepasapresentation
```

