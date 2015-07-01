#! /usr/bin/python3
import re

#Hangul to English matching
names = {
	"Yoomis.Room":re.compile(r"유미의 방"),
	"Snow.Flower":re.compile(r"눈꽃"),
	"Save.the.Last.Dance":re.compile(r"마지막 춤은 나와함께"),
	"Tears.of.Diamond":re.compile(r"다이아몬드의 눈물"),
	"All.About.Eve":re.compile(r"이브의 모든것"),	
	"My.Love":re.compile(r"마이 러브"),
	"Sassy.Girl.Choon.Hyang":re.compile(r"쾌걸 춘향"),
	"Oh.Feel.Young":re.compile(r"오\!필승 봉순영"),
	"Lawyers":re.compile(r"변호사들"),
	"HyoYeons.One.Million.Likes":re.compile(r"효연의 백만 라이크"),
	"The.Time.We.Were.Not.In.Love":re.compile(r"너를 사랑한 시간"),
	"The.Genius.Grand.Final":re.compile(r"더 지니어스 그랜드 파이널"),
	"Goodbye.Sadness":re.compile(r"슬픔이여안녕"),
	"My.Sweetheart.My.Darling":re.compile(r"어여쁜 당신"),
	"Red.Chair":re.compile(r"빨간의자"),
	"Celebrity.Biography":re.compile(r"셀러브리티 바이오그래피"),
	"AfreecaTV.AOA.Livechatting":re.compile(r"아프리카TV AOA 라이브채팅"),
	"The.Accidental.Couple":re.compile(r"그저\s*바라보다가"),
	"Tree.With.Deep.Roots":re.compile(r"뿌리깊은 나무"),
	"Discovery.of.Love":re.compile(r"연애의 발견"),
	"The.Moon.That.Embraces.The.Sun":re.compile(r"해를 품은 달"),
	"Webdrama":re.compile(r"웹드라마"),
	"The.Concert":re.compile(r"더 콘서트"),
	"Age.of.Warriors":re.compile(r"무인시대"),
	"Secret.Weapon":re.compile(r"비밀병기\s*그녀"),
	"History.Special":re.compile(r"역사스페셜"),
	"Masterchef.Korea":re.compile(r"마스터셰프 코리아"),
	"Glorious.Day":re.compile(r"기분 좋은 날"),
	"Only.Love":re.compile(r"사랑만 할래"),
	"My.Mother.is.a.Daughter.In.Law":re.compile(r"어머님은 내 며느리"),
	"I.Remember.You":re.compile(r"너를 기억해"),
	"Top.10.Songs":re.compile(r"가요 TOP 10"),
	"I.am.also.Film.Director":re.compile(r"나도 영화 감독이다"),
	"My.Beautiful.Bride":re.compile(r"아름다운 나의\s*신부"),
	"Boarding.House.24":re.compile("하숙24번지"),
	"Whats.Up.Fox":re.compile(r"여우야 뭐하니"),
	"Bodyguard":re.compile(r"보디가드"),
	"Golden.Time":re.compile(r"골든\s*타임"),
	"Yi.San":re.compile(r"이산"),
	"My.Daughter.Seo.Young":re.compile(r"내 딸 서영이"),
	"Temptation.of.Wife":re.compile(r"아내의 유혹"),
	"Jewel.in.the.Palace":re.compile(r"대장금"),
	"School.1":re.compile(r"학교 1"),
	"Sunflower":re.compile(r"해바라기"),
	"Goodbye.My.Love":re.compile(r"안녕\s*내사랑"),
	"Robber":re.compile(r"불한당"),
	"The.Princess.Man":re.compile(r"공주의 남자"),
	"See.and.See.Again":re.compile(r"보고 또 보고"),
	"Best.Wedding":re.compile(r"최고의 결혼"),
	"Fight":re.compile(r"맞짱"),
	"Hidden.Identity":re.compile(r"신분을 숨겨라"),
	"King.Geunchogo":re.compile(r"근초고왕"),
	"The.Great.Wives":re.compile(r"위대한 조강지처"),
	"Medical.Brothers":re.compile(r"의가형제"),
	"Brilliant.Legacy":re.compile(r"찬란한 유산"),
	"Hidden.Singer":re.compile(r"히든싱어"),
	"King.And.Queen":re.compile(r"왕과\s*비"),
	"It.Was.Love":re.compile(r"사랑했나봐"),
	"My.Fair.Lady":re.compile(r"아가씨를 부탁해"),
	"Full.House":re.compile(r"풀하우스"),
	"Hometown.Legends":re.compile(r"전설의 고향"),
	"Romance":re.compile(r"^로망스"),
	"Again":re.compile(r"^어게인"),
	"Papa":re.compile(r"파파"),
	"Three.Guys.and.Three.Girls":re.compile(r"남자셋\,여자셋"),
	"Im.Kkeok.Jung":re.compile(r"임꺽정"),
	"Inside.SuperRace":re.compile(r"인사이드 슈퍼레이스"),
	"Restaurant.of.100.Years":re.compile(r"백년식당"),
	"Girlfriend.Look.After.Our.Dog":re.compile(r"여자친구! 강아지를 부탁해"),
	"Death.Debate":re.compile(r"사망토론"),
	"Let.Me.In":re.compile(r"Let 미인"),
	"Love.Letter":re.compile(r"리얼로망스 연애편지"),
	"The.4th.Republic":re.compile(r"제4공화국"),
	"Sunny.Days.of.Youth":re.compile(r"젊은이의 양지"),
	"HIT.Homicide.Investigation.Team":re.compile(r"히트"),
	"Oh.Ja.Ryong.is.Coming":re.compile(r"오자룡이 간다"),
	"Great.Recipe":re.compile(r"대단한 레시피"),
	"The.Returm.of.Hwang.Geum.Bok":re.compile(r"돌아온 황금복"),
	"High.Society":re.compile(r"상류사회"),
	"Angels.Revenge":re.compile(r"천상여자"),
	"Famous.Princesses":re.compile(r"소문난\.*칠공주"),
	"Alone.in.Love":re.compile(r"연애시대"),
	"Pasta":re.compile(r"파스타"),
	"Life.is.Beautiful":re.compile(r"인생은 아름다워"),
	"The.Last.Game":re.compile(r"마지막승부"),
	"Bokbulbok.Show":re.compile(r"복불복 쇼"),
	"Golden.Tower":re.compile(r"황금거탑"),
	"The.Greatest.Love":re.compile(r"최고의 사랑"),
	"Autumn.in.My.Heart":re.compile(r"가을동화"),
	"Huh.Joon":re.compile(r"허준"),
	"Horse.Doctor":re.compile(r"^마의"),
	"Big":re.compile(r"^빅"),
	"Comedy.Stations":re.compile(r"웃음 충전소"),
	"Chuno":re.compile(r"추노"),
	"Goong":re.compile(r"^궁"),
	"Feelings":re.compile(r"느낌"),
	"God.of.Study":re.compile(r"공부의 신"),
	"Love.in.your.Bosom":re.compile(r"사랑을 그대품안에"),
	"The.3rd.Republic":re.compile(r"제\s*3공화국"),
	"MBC.Best.Theater":re.compile(r"베스트\s*극장"),
	"The.Chaser":re.compile(r"추적자"),
	"Pumpkin.Seed":re.compile(r"호박씨"),
	"Match":re.compile(r"^짝"),
	"Chok.Chok.Oppas":re.compile(r"촉촉한 오빠들"),
	"White.Swan":re.compile(r"화이트 스완"),
	"Suspicious.Dog.Cafe":re.compile(r"수상한 애견카페"),
	"Korean.Music.Festival":re.compile(r"국악한마당"),
	"Oh.Halmae":re.compile(r"농촌드라마 오 할매"),
	"Dream.Concert":re.compile(r"드림콘서트"),
	"Assorted.Gems":re.compile(r"보석 비빔밥"),
	"Tempted.Again":re.compile(r"탐나는도다"),
	"Myung.Wol.the.Spy":re.compile(r"스파이 명월"),
	"Beloved.Eun.Dong":re.compile(r"사랑하는 은동아"),
	"49.Days":re.compile(r"49일"),
	"High.Kick.Through.The.Roof":re.compile(r"지붕 뚫고 하이킥"),
	"Capital.Scandal":re.compile(r"경성스캔들"),
	"Protect.the.Boss":re.compile(r"보스를 지켜라"),
	"Emperor.Wang.Gun":re.compile(r"태조\s*왕건"),
	"The.Voice.Of.Korea":re.compile(r"보이스 코리아"),
	"Air.City":re.compile(r"에어시티"),
	"Lie.to.Me":re.compile(r"내게 거짓말을 해봐"),
	"A.Mans.Story":re.compile(r"남자 이야기"),
	"Hong.Gil.Dong":re.compile(r"쾌도 홍길동"),
	"Cheongdamdong.Alice":re.compile(r"청담동 앨리스"),
	"Mask":re.compile(r"가면"),
	"Sungkyunkwan.Scandal":re.compile(r"성균관 스캔들"),
	"The.Woman.Who.Still.Wants.To.Marry":re.compile(r"아직도 결혼하고 싶은 여자"),
	"Royal.Family":re.compile(r"로열 패밀리"),
	"The.God.of.Music":re.compile(r"음악의 신"),
	"The.51st.BaekSang.Arts.Awards":re.compile(r"제51회 백상예술대상"),
	"New.Tales.of.Gisaeng":re.compile(r"신기생뎐"),
	"Blue.Mist":re.compile(r"푸른\s*안개"),
	"City.Hunter":re.compile(r"시티헌터"),
	"Ruby.Ring":re.compile(r"루비반지"),
	"7th.Grade.Civil.Servant":re.compile(r"7급 공무원"),
	"Queen.of.Reversals":re.compile(r"역전의 여왕"),
	"Haeundae.Lovers":re.compile(r"해운대 연인들"),
	"Endless.Love":re.compile(r"끝없는 사랑"),
	"Miss.Daegu.Competition":re.compile(r"미스 대구 선발대회"),
	"Snow.White":re.compile(r"백설공주"),
	"Robber":re.compile(r"불한당"),
	"You.Are.My.Destiny":re.compile(r"너는 내 운명"),
	"Ireland":re.compile(r"아일랜드"),
	"Man.Of.Honor":re.compile(r"영광의 재인"),
	"First.Love":re.compile(r"첫사랑"),
	"Mary.Stayed.Out.All.Night":re.compile(r"매리는 외박중"),
	"Successful.Story.of.a.Bright.Girl":re.compile(r"명랑소녀( 성공기)*"),
	"The.King.2.Hearts":re.compile(r"더 킹 투\s*하츠"),
	"Queen.of.Ambition":re.compile(r"야왕"),
	"Faith":re.compile(r"신의"),
	"Mr.Baek.The.Homemade.Food.Master":re.compile(r"집밥\s*백선생"),
	"House.of.10":re.compile(r"모델하우스"),
	"5Days.of.Summer":re.compile(r"5일간의 썸머"),
	"Korean.Food.War":re.compile(r"한식대첩"),
	"Masked.Prosecutor":re.compile(r"복면검사"),
	"Fox.and.Cotton.Candy":re.compile(r"여우와\s*솜사탕"),
	"Eyes.of.Dawn":re.compile(r"여명의 눈동자"),
	"The.Birth.of.the.Rich":re.compile(r"부자의\s*탄생"),
	"The.Painter.of.the.Wind":re.compile(r"바람의 화원"),
	"Dr.Jin":re.compile(r"닥터 진"),
	"Eves.Love":re.compile(r"이브의 사랑"),
	"A.Daughter.Just.Like.You":re.compile(r"딱 너\s*같은 딸"),
	"Running":re.compile(r"심장이\s*뛴다"),
	"Ruler.of.your.own.World":re.compile(r"네\s*멋대로\s*해라"),
	"Surgeon.Bong.Dal.Hee":re.compile(r"외과의사\s*봉달희"),
	"Producer":re.compile(r"프로듀사"),
	"Orange.Marmalade":re.compile(r"오렌지 마말레이드"),
	"Why.Cant.We.Stop.Them":re.compile(r"웬만해선 그들을 막을 수 없다"),
	"Warm.And.Cozy":re.compile(r"맨도롱\s*또(똣|돗)"),
	"Protect.the.Family":re.compile(r"가족을 지켜라"),
	"Improvisation":re.compile(r"순발력"),
	"Playful.Kiss":re.compile(r"장난스런키스"),
	"Lady.Action":re.compile(r"레이디 액션"),
	"Secret.Angel":re.compile(r"비밀천사"),
	"Reckless.Challenge":re.compile(r"무모한도전"),
	"Ex.Girlfriend.Club":re.compile(r"구여친클럽"),
	"K-Star.Report":re.compile(r"한류스타 리포트"),
	"Rediscovery.of.Immortal.Song":re.compile(r"불후의 재발견"),
#	"Asia.Prism":re.compile(r"아시아 프리즘"),
	"My.Sunshine":re.compile(r"마이 선샤인"),
	"Sixteen":re.compile(r"식스틴"),
	"Cool.Kkadang":re.compile(r"쿨까당"),
	"Birds.Dont.Cry":re.compile(r"울지 않는 새"),
	"Good.Life":re.compile(r"통일준비 생활백서 잘 살아보세"),
	"Police.Station":re.compile(r"경찰청 사람들"),
	"KimJaeDongs.Talk.To.You":re.compile(r"김제동의 톡투유"),
	"Seventeen.Project":re.compile(r"세븐틴 프로젝트"),
#	"Music.Video.Bank":re.compile(r"뮤비뱅크"),
	"Slimmy.Lunch.Box":re.compile(r"날씬한\s*도시락"),
	"The.Brave.Teenagers":re.compile(r"고교10대천왕"),
	"The.Lawyers.of.the.Great.Republic.Korea":re.compile(r"대\~한민국 변호사"),
	"Bachelor.While.on.a.Date":re.compile(r"총각 연애하다"),
	"I.Introduce.My.Father":re.compile(r"아빠를 소개합니다"),
	"Go.Go.With.Unnie":re.compile(r"언니랑 고고"),
	"Gu.Family.Book":re.compile(r"구가의 서"),
	"Who.Are.You.School.2015":re.compile(r"후아유(-|\s){1,3}학교 2015"),
	"More.Charming.By.The.Day":re.compile(r"볼수록 애교만점"),
	"Sandglass":re.compile(r"모래시계"),
	"My.Rosy.Life":re.compile(r"장미빛 인생"),
	"1.VS.100":re.compile(r"1 대 100"),
	"Mom.Is.Watching":re.compile(r"엄마가 보고있다"),
	"Moonshine":re.compile(r"문샤인"),
	"Heart.A.Tag":re.compile(r"하트어택"),
	"Nympho.Island":re.compile(r"색녀도"),
	"Love.Switch":re.compile(r"러브스위치"),
	"K-Pop.Star":re.compile(r"케이팝스타"),
	"Divorce.Lawyer.in.Love":re.compile(r"이혼변호사는 연애중"),
	"A.Look.At.Myself":re.compile(r"나를 돌아봐"),
	"Miss.Mermaid":re.compile(r"인어아가씨"),
	"The.Three.Musketeers":re.compile(r"해외걸작드라마 삼총사"),
	"Make.a.Woman.Cry":re.compile(r"여자를 울려"),
	"Hilarious.Housewives":re.compile(r"태희혜교지현이"),
	"Catch.Music.if.you.can":re.compile(r"캐치 뮤직 이프 유 캔"),
	"Talkshow.Parents":re.compile(r"토크쇼 부모"),
#	"Mask.King":re.compile(r"복면가왕"),
	"MiSaGo":re.compile(r"두근두근 감동카메라 미사고"),
	"The.Body.Show":re.compile(r"더 바디쇼"),
	"Open.Up":re.compile(r"맴을 열어봐"),
	"My.Unfortunate.Boyfriend":re.compile(r"나의 유감스러운 남자친구"),
	"Splendid.Politics":re.compile(r"화정"),
	"Style.For.You":re.compile(r"스타일 포유"),
	"Exciting.India":re.compile(r"두근두근 인도"),
	"Mother.Person":re.compile(r"엄마사람"),
	"Dancing.9":re.compile(r"댄싱9"),
	"The.Superman.Age":re.compile(r"초인시대"),
	#drama
	"Hair.Day":re.compile(r"머리 심는 날"),
	"Funny.Girl":re.compile(r"웃기는 여자"),
	"Mr.Back":re.compile(r"미스터 백"),
	"Pinocchio":re.compile(r"피노키오"),
	"The.Kings.Face":re.compile(r"왕의 얼굴"),
	"Cheongdamdong.Scandal":re.compile(r"청담동 스캔들"),
	"Make.a.Wish":re.compile(r"소원을 말해봐"),
	"Lady.of.the.Storm":re.compile(r"폭풍의 여자"),
	"Healer":re.compile(r"힐러"),
	"Family.Secrets":re.compile(r"가족의 비밀"),
	"Punch":re.compile(r"펀치|때려"),
	"Sunam.Girls.High.School.Detectives":re.compile(r"선암여고\s*탐정단"),
	"Valid.Love":re.compile(r"일리\s*있는 사랑"),
	"Pride.and.Prejudice":re.compile(r"오만과 편견"),
	"Tears.of.Heaven":re.compile(r"천국의 눈물"),
	"What.happens.to.my.Family":re.compile(r"가족끼리 왜 이래"),
	"Rosy.Lovers":re.compile(r"장미빛 연인들"),
	"The.legend.of.the.Witch":re.compile(r"전설의 마녀"),
	"Dr.Frost":re.compile(r"닥터 프로스트"),
#	"Misaeng":re.compile(r"미생"),	
	"Misaengmul":re.compile(r"미생물"),
	"Birth.of.a.Beauty":re.compile(r"미녀의\s*탄생"),
	"Best.Wedding":re.compile(r"최고의 결혼"),
	"Apgujeong.Midnight.Sun":re.compile(r"압구정 백야"),
	"Maids":re.compile(r"하녀들"),
	"Modern.Farmer":re.compile(r"모던파머"),
	"Secret.Door":re.compile(r"비밀의 문"),
	"Bad.Guys":re.compile(r"나쁜 녀석들"),
	"Hometown.over.the.hill":re.compile(r"산너머 남촌에는 2"),
	"Tomorrow.Cantabile":re.compile(r"내일도 칸타빌레"),
	"Liar.Game":re.compile(r"라이어게임"),
	"Queen.of.Housewives":re.compile(r"내조의 여왕"),
	"Love.and.Secret":re.compile(r"달콤한 비밀"),
	"You.are.the.only.one":re.compile(r"당신만이 내사랑"),
	"Run.Jang.Mi":re.compile(r"달려라 장미"),
	"Abiding.Love.Dandelion":re.compile(r"TV소설 일편단심 민들레"),
	"Powerful.Opponents":re.compile(r"강적들"),
	"Ok.Family":re.compile(r"옥이네"),
	"Sharp":re.compile(r"반올림"),
	"Sense.King":re.compile(r"눈치왕"),
	"The.Family.is.coming":re.compile(r"떴다 패밀리"),
	"Special.Crimes.Force":re.compile(r"특수사건전담반"),
	"April.Kiss":re.compile(r"4월의\s*키스"),
	"Iron.Lady.Cha":re.compile(r"불굴의 차여사"),
	"Enchanting.Neighbor":re.compile(r"황홀한 이웃"),
	"Mackerel.Run":re.compile(r"달려라 고등어"),
	"Me.Too.Flower":re.compile(r"나도, 꽃!"),
	"Swallow.the.Sun":re.compile(r"태양을 삼켜라"),
	"My.Husband.got.a.Family":re.compile(r"넝쿨째 굴러온 당신"), 
	"The.Invisible.Man":re.compile(r"투명인간"),
	"Kill.Me.Heal.Me":re.compile(r"킬미,* 힐미"),
	"New.Nonstop":re.compile(r"뉴논스톱"),
	"Hello.My.Teacher":re.compile(r"건빵선생과 별사탕"),
	"I.Need.Romance":re.compile(r"로맨스가 필요해"),
#	"Spy":re.compile(r"스파이"),
	"The.Sons.of.Sol.Pharmacy.House":re.compile(r"솔약국집아들들"),
	"Heart.to.Heart":re.compile(r"하트\s*투\s*하트"),
	"Perseverance.Goo.Hae.Ra":re.compile(r"칠전팔기 구해라"),
	"Wish.Upon.a.Star":re.compile(r"별은 내가슴에"),
	"Shoot.for.the.Star":re.compile(r"별을\.*쏘다"),
	"Tomato":re.compile(r"토마토"),
	"That.Winter.the.Wind.Blows":re.compile(r"그\s*겨울 바람이 분다"),
	"Crazy.For.You":re.compile(r"사랑에 미치다"),
	"Full.House":re.compile(r"풀하우스"),
	"Smile.You":re.compile(r"그대 웃어요"),
	"Honest.Living":re.compile(r"똑바로 살아라"),
	"Gods.Quiz":re.compile(r"신의 퀴즈"),
	"A.Love.To.Kill":re.compile(r"이\s*죽일놈의\s*사랑"),
	"The.Man.Who.Cant.Get.Married":re.compile(r"결혼 못하는 남자"),
	"Mom.Has.Grown.Horns":re.compile(r"엄마가 뿔났다"),
	"My.Heart.is.Twinkling":re.compile(r"내 마음 반짝반짝"),
	"My.Mans.Woman":re.compile(r"내 남자의 여자"),
	"Vampire.Prosecutor.S02":re.compile(r"뱀파이어 검사2"),
	"Beethoven.Virus":re.compile(r"베토벤 바이러스"),
	"School.4":re.compile(r"학교4"),
	"Witch.Amusement":re.compile(r"마녀유희"),
	"Basketball":re.compile(r"빠스껫볼"),
	"Shine.Or.Go.Crazy":re.compile(r"빛나거나 미치거나"),
	"Reply.1994":re.compile(r"응답하라 1994"),
	"Shark":re.compile(r"상어"),
	"Lovers.in.Paris":re.compile(r"파리의 연인"),
	"Empire.of.Gold":re.compile(r"황금의 제국"),
	"Queen.Seon.Deok":re.compile(r"선덕여왕"),
	"The.Immortal.Lee.Soon.Shin":re.compile(r"불멸의 이순신"),
	"Hyde.Jekyll.Me":re.compile(r"하이드 지킬\,* 나"),
	"Beating.Heart":re.compile(r"떨리는 가슴"),
	"Dream.High":re.compile(r"드림하이"),
	"Bridal.Mask":re.compile(r"각시탈"),
	"Familys.Honor":re.compile(r"가문의 영광"),
	"Gap.Dong":re.compile(r"갑동이"),
	"Brave.Family":re.compile(r"용감한\s*가족"),
	"City.of.the.Sun":re.compile(r"태양의 도시"),
	"You.have.fallen.for.me":re.compile(r"넌 내게 반했어"),
	"Fool.For.You":re.compile(r"호구의 사랑"),
	"Thank.You.Son":re.compile(r"고맙다 아들아"),
	"Incarnation.Of.Money":re.compile(r"남자의 자격"),
	"Jingbirok":re.compile(r"징비록"),
	"Blood":re.compile(r"블러드"),
	"Flirty.Boy.And.Girl":re.compile(r"썸남썸녀"),
	"Cupid.Factory":re.compile(r"큐피드 팩토리"),
	"Came.to.Me.and.Became.a.Star":re.compile(r"나에게로 와서 별이 되었다"),
	"Bluebirds.House":re.compile(r"파랑새의 집"),
	"Life.Tracker.Lee.Jae.Goo":re.compile(r"인생추적자 이재구"),
	"Heard.It.Through.the.Grapevine":re.compile(r"풍문으로 들었소"),
	"Unkind.Women":re.compile(r"착하지 않은 여자들"),
	"Snowy.Road":re.compile(r"눈길"),
	"TV.Novel.On.a.Blue.Day":re.compile(r"TV소설 그래도 푸르른 날에"),
	"Super.Daddy.Yeol":re.compile(r"슈퍼대디 열"),
	"Flower.of.the.Queen":re.compile(r"여왕의 꽃"),
	"Stay.Still":re.compile(r"가만히 있으라"),
	"Angry.Mom":re.compile(r"앵그리맘"),
	"A.Great.Story":re.compile(r"위대한 이야기"),
	"The.Wind.Blows.In.The.Direction.Of.Hope":re.compile(r"바람은 소망하는 곳으로 분다"),
	"Missing.Noir.M":re.compile(r"실종\s*느와르.*M"),
	"Falling.For.Innocence":re.compile(r"순정에 반하다"), #prev Genuine.Love
	"The.Lover":re.compile(r"더 러버"),
	"Flower.Boys.Next.Door":re.compile(r"이웃집 꽃미남"),
	"Love.From.Today":re.compile(r"오늘부터 사랑해"),
	"Lets.Eat":re.compile(r"식샤를\s*합시다"),
	#ent
	"Superstar.K6":re.compile(r"슈퍼스타K"),
	"Hello.Stranger":re.compile(r"헬로 이방인"),
	"Happy.Together":re.compile(r"해피\s*투게더"),
	"Oh.My.Baby":re.compile(r"오(\!)* 마이 베이비"),
	"Witch.Hunt":re.compile(r"마녀사냥"),
	"Infinity.Challenge":re.compile(r"무한도전"),
	"We.Got.Married":re.compile(r"우리\s*결혼했어요"),
	"Music.Core":re.compile(r"(쇼!)*\s*음악중심"),
	"3.Meals.a.Day":re.compile(r"삼시세끼"),
	"Star.Married.Couple":re.compile(r"자기야\-*\s*백년손님"),
	"A.very.curious.story":re.compile(r"아궁이"),
	"Cook.King.Korea":re.compile(r"쿡킹 코리아"),
	"World.Changing.Quiz":re.compile(r"세바퀴"),
	"Super.Idol.Chartshow":re.compile(r"슈퍼 아이돌 차트쇼"),
	"Song.Festival":re.compile(r"가요대축제"),
	"Entertainment.Awards":re.compile(r"연예대상"),
	"Always.Cantare":re.compile(r"언제나 칸타레"),
	"Cartalk.Show.S.":re.compile(r"카톡쇼 S"),
	"Cartalk.Show.X.":re.compile(r"카톡쇼 X"),
	"My.Bodys.Usage.Manual":re.compile(r"내 몸 사용 설명서"),
	"Lets.go.to.School":re.compile(r"학교\s*다녀오겠습니다"),
	"Love.Unification.of.South.Man.and.North.Women":re.compile(r"(애정통일 )*남남북녀"),
	"My.young.Tutor":re.compile(r"띠동갑내기 과외하기"),
	"Law.of.the.Jungle":re.compile(r"정글의 법칙"),
#	"Law.of.the.Jungle.in.Brazil":re.compile(r"정글의 법칙 in 브라질"),
#	"Law.of.the.Jungle.in.Indian.Ocean":re.compile(r"정글의 법칙 in 인도양"),
	"Inkigayo":re.compile(r"인기가요"),
	"Star.King":re.compile(r"놀라운 대회 스타킹"),
	"Actresses.Secret.Travel.in":re.compile(r"여우 비행 인"),
	"Good.Sunday.K-Pop.Star":re.compile(r"(일요일이 좋다-)*K팝스타"),
	"Good.Sunday.Running.Man":re.compile(r"(일요일이 좋다\s*-\s*)*런닝맨"),
#	"Good.Sunday.Survival.Audition.K-Pop.Star":re.compile(r"일요일이 좋다-서바이벌 오디션 K팝스타"),
	"The.Return.of.Superman":re.compile(r"슈퍼맨이 돌아왔다"),
#	"Our.Sunday.Night.King.of.Masked.Singers":re.compile(r"일밤 1부 복면가왕"),
	"Our.Sunday.Night.Daddy.Where.Are.You.Going":re.compile(r"(일밤 1부 )*아빠\!* 어디가"),
	"Our.Sunday.Night.Real.Man":re.compile(r"(일밤 2부 )*진짜\s*사나이"),
	"Our.Sunday.Night.Animals":re.compile(r"일밤 1부 애니멀즈"),
	"Saturday.Freedom.Immortal.Music":re.compile(r"불후의 명곡 전설을 노래하다"),
	"Happy.Sunday.2Days.1Night":re.compile(r"(해피\s*선데이\s*-\s*)*1박2일"),
	"Comedy.Big.League":re.compile(r"코미디\s*빅리그"),
	"Smile.People":re.compile(r"웃음을 찾는 사람들"),
	"Gag.Concert":re.compile(r"개그콘서트"),
	"I.Live.Alone":re.compile(r"나 혼자 산다"),
	"SuperJuniorM.Guest.House":re.compile(r"슈퍼주니어M 게스트하우스"),
	"Lets.Go.Dream.Team":re.compile(r"출발\s*드림팀"),
	"Extreme.Surprise":re.compile(r"익스트림 서프라이즈"),
	"Mysterious.TV.Surprise":re.compile(r"신비한TV 서프라이즈"),
	"Concert.7080":re.compile(r"(배철수의 )*콘서트\s*7080"),
	"Salon.de.raison":re.compile(r"속사정\s*쌀롱"),
	"Take.Care.of.the.Fridge":re.compile(r"냉장고를\s*부탁해"),
	"Abnormal.Summit":re.compile(r"비정상회담"),
	"Hello.Counselor":re.compile(r"(대국민 토크쇼 )*안녕하세요"),
	"Healing.Camp":re.compile(r"힐링캠프( 기쁘지 아니한가)*"),
	"Safety.First":re.compile(r"위기탈출 넘버원"),
	"Golden.Egg":re.compile(r"고수의 비법 황금알"),
	"Trot.Festival":re.compile(r"트로트 대축제"),
	"National.Song.Contest":re.compile(r"전국노래자랑"),
	"Master.of.Life":re.compile(r"생활의 달인"),
	"True.Justice":re.compile(r"정의본색"),
	"Now.on.my.way.to.meet.you":re.compile(r"이제 만나러\s*갑니다"),
	"100.Song":re.compile(r"백인백곡 끝까지 간다"),
	"9.Store":re.compile(r"살림9단의 만물상"),
	"Today.Menu":re.compile(r"오늘 뭐 먹지"),
	"Talk.Show.Dongchimi":re.compile(r"속풀이쇼 동치미"),
	"Medical.Recipeshow.Atlas":re.compile(r"메디컬 레시피쇼 아틀라스"),
	"With.You":re.compile(r"님과 함께"),
	"Drama.Awards":re.compile(r"연기대상"),
	"Daechan.Life":re.compile(r"대찬인생"),
	"Cool.Kiz.on.the.Block":re.compile(r"우리동네 예체능"),
	"After.School.Bokbulbok":re.compile(r"방과후 복불복"),
	"Music.Festival":re.compile(r"가요대제전"),
	"The.4th.Weekly.Idol.Awards":re.compile(r"제4회.주간아이돌 어워즈"),
	"New.Years.Eve.Concert.Creating.Hope.Korea":re.compile(r"새해맞이 음악회 희망창조, 코리아"),
	"Wedding.Story":re.compile(r"결혼 이야기"),
	"War.Of.The.Worlds":re.compile(r"썰전"),
	"Power.to.Children":re.compile(r"아이에게 권력을"),
	"I.have.a.Gods.Body":re.compile(r"나는 몸신이다( 베스트)*"),
	"Capture.the.Moment.How.is.that.possible":re.compile(r"순간포착 세상에 이런일이"),
	"Music.Bank":re.compile(r"뮤직뱅크"),
	"YooHeeYeols.Sketchbook":re.compile(r"유희열의 스케치북"),
	"Talk.with.Star.in.Taxi":re.compile(r"현장토크쇼 (택시|TAXI)"),
	"Future.Predictions.Variety.Butterfly.Effect":re.compile(r"미래예측 버라이어티 나비효과"),
	"Sweden.Laundry":re.compile(r"스웨덴 세탁소"),
	"I.love.Movie":re.compile(r"영화가 좋다"),
	"Movieworld":re.compile(r"접속! 무비월드"),
	"Entertainment.Weekly":re.compile(r"연예가\s*중계"),
	"The.Human.Condition":re.compile(r"인간의 조건"),
	"Start.Video.Tour":re.compile(r"출발! 비디오 여행"),
	"Star.Junior.Show":re.compile(r"스타주니어쇼 붕어빵"),
	"TV.Zoo":re.compile(r"TV 동물농장"),
	"Find.Delicious.TV":re.compile(r"찾아라!\s*맛있는 TV"),
	"Vienna.Philharmonic.Orchestra.New.Years.Concert":re.compile(r"비엔나 필하모닉 오케스트라 신년음악회"),
	"Section.TV":re.compile(r"섹션TV 연예통신"),
	"Gourmet.Road":re.compile(r"식신로드"),
	"Top.Gear.Korea":re.compile(r"탑\s*기어 코리아"),
	"Yaman.TV":re.compile(r"야만TV"),
	"Roommate":re.compile("룸메이트"),
	"Lord.of.the.Thumb":re.compile(r"엄지의 제왕"),
	"Gayo.Stage":re.compile(r"가요무대"),
	"Birth.of.a.Mother":re.compile(r"엄마의 탄생"),
	"Vitamin":re.compile(r"비타민"),
	"Golden.Fishery":re.compile(r"황금어장\-*\s*라디오스타"),
	"Eco.Village":re.compile(r"에코빌리지 즐거운 가"),
	"Secret.Love":re.compile(r"비밀연애"),
	"Kids.are.Lifes.Blessing":re.compile(r"유자식\s*상팔자"),
	"Live.Entertainment.Weekly":re.compile(r"한밤의 TV연예"),
	"M.Countdown.Begins":re.compile(r"엠카운트다운 비긴즈"),
	"Accused.by.Kang.Yong.Suk":re.compile(r"강용석의 고소한"),
	"Weekly.Idol":re.compile(r"주간\s*아이돌"),
	"Baby.100Years.Guests":re.compile(r"자기야 - 백년손님"),
	"Sistar.Showtime":re.compile(r"씨스타의\s*쇼타임"),
	"Turn.to.the.King":re.compile(r"켠김에 왕까지"),
	"Determined.to.Watch.the.Premiere":re.compile(r"작정하고 본방사수"),
	"Hyung.Don.Dae.Joons.Hit.Machine":re.compile(r"형돈이와 대준이의 히트제조기"),
	"King.of.Idol":re.compile(r"아이돌의\s*제왕"),
	"Who.is.the.Better.Magician":re.compile(r"누가 누가 잘하나"),
	"Open.Concert":re.compile(r"열린음악회"),
	"Global.Request.Show.A.Song.For.You":re.compile(r"글로벌 리퀘스트 쇼 어송포유"),
	"Doctors.Warning":re.compile(r"닥터의 경고"),
	"Shopper.Man":re.compile(r"나르는 쇼퍼맨"),
	"Cheeky.Interview.4Things.Show":re.compile(r"발칙한 인터뷰 4가지 쇼"),
	"Revealing.a.List.of.Names":re.compile(r"명단공개"),
	"Showtime.Burning.the.Beast":re.compile(r"쇼타임\-버닝더비스트"),
	"We.Got.Married.Kwanghee.Sunhwa":re.compile(r"광희 선화 결혼이야기"),
	"We.Got.Married.SonNaeun.Taemin":re.compile(r"우결-손나은,태민"),
	"We.Got.Married.Junhee.Jinwoon":re.compile(r"고준희 진운 결혼이야기"),
	"We.Got.Married.Eunjung.Jangwoo":re.compile(r"은정 장우"),
	"Star.News":re.compile(r"스타뉴스"),
	"Tasty.Road":re.compile(r"테이스티 로드"),
	"Dissecting.Entertainment.The.Women.Trio":re.compile(r"연예 해부 여기자 삼총사가 간다"),
	"The.Demand.Of.Luxurious.Food":re.compile(r"수요미식회"),
	"The.29th.Golden.Disk.Awards.in.Beijing":re.compile(r"제29회 골든디스크 어워즈 인 베이징"),
	"The.24th.Seoul.Music.Awards":re.compile(r"제24회 하이원 서울가요대상"),
	"MTV.The.Show":re.compile(r"더\s*쇼"),
	"A.Celebrity.Lives.In.Our.House":re.compile(r"우리집에 연예인이 산다"),
	"Style.Live":re.compile(r"스타일 라이브"),
	"Olive.Show":re.compile(r"올리브쇼"),
	"Brave.Reporters":re.compile(r"용감한 기자들"),
	"Please.Permit":re.compile(r"허락해 주세요"),
	"Culture.Bigbang.The.Concert.Of.Yoon.Gun":re.compile(r"문화빅뱅 윤건의 더 콘서트"),
	"A.Skill.Of.Wisdom.Cane":re.compile(r"지혜의 한 수 회초리"),
	"Jung.Yonghwas.Hologram":re.compile(r"정용화의\s*홀로그램"),
	"Unpretty.Rapstar":re.compile(r"언프리티\s*랩스타"),
	"I.Am.A.Singer":re.compile(r"나는 가수다"),
	"Dating.Alone":re.compile(r"나홀로 연애중"),
	"TV.Law.Firm":re.compile(r"TV로펌 법대법"),
	"Ultimate.Quiz.Show.Q":re.compile(r"최강연승 퀴즈쇼 큐"),
	"Space.Sympathy":re.compile(r"스페이스 공감"),
	"Where.is.my.Friends.Home":re.compile(r"내\s*친구의\s*집은\s*어디인가"),
	"My.Little.Television":re.compile(r"마이\s*리틀\s*텔(레|리)비전|마리텔"),
	"Independent.Cinema":re.compile(r"독립영화관"),
	"Car.Center":re.compile(r"카(\!)*센터"),
	"Saturday.Night.Live.Korea":re.compile(r"(SNL|snl)\s*코리아"),
	"VIXX.One.Fine.Day":re.compile(r"빅스의 어느 멋진날"),
	"AOA.One.Fine.Day":re.compile(r"AOA\s*어느\s*멋진날"),
	"Shin.Dong.Yups.Bachelor.Party":re.compile(r"신동엽과 총각파티"),
	"Romantic.Show.Yesterday":re.compile(r"낭만쇼 예스터데이"),
	"The.Golden.Bell.Challenge":re.compile(r"도전 골든벨"),
	"Star.Golden.Bell":re.compile(r"스타 골든벨"),
	"Code.Zero":re.compile(r"코드제로"),
	"Challenge.1000.Songs":re.compile(r"도전 1000곡"),
	"A.Dinner.Of.Fisherman":re.compile(r"어부의\s*만찬"),
	"Burning.Youth":re.compile(r"불타는 청춘"),
	"Mystery.Music.Show.Mask.King":re.compile(r"(미스터리 음악쇼 )*복면가왕"),
	"Tiger.Mask.Magic.Show":re.compile(r"타이거 마스크 매직쇼"),
	"Return.To.Farming.Project":re.compile(r"귀농프로젝트"),
	"Idolstar.Championship":re.compile(r"아이돌스타 선수권대회"),
	"Idolstar.Futsal.Archery.Athletics.Basketball.Championship":re.compile(r"아이돌스타 육상 농구 풋살 양궁 선수권\s*대회"),
	"Running.Toward.Tomorrow":re.compile(r"내일을 향해 뛰어라"),
	"Noisy.Animal.Theater":re.compile(r"와글와글 동물극장"),
	"Take.Care.of.Dad":re.compile(r"아빠를 부탁해"),
	"Infinite.Challenger":re.compile(r"토요일 토요일은 무도다"),
	"Kim.Jae.Dongs.Talk.To.You.Dont.You.Worry":re.compile(r"김제동의 톡투유 걱정 말아요 그대"),
	"Saturday.Is.For.Singers":re.compile(r"(토요일! 토요일은 가수다|토토가)"),
	"Yeongjae.Balguldan":re.compile(r"영재\s*발굴단"),
	"LeeSeungHwan.Concert.Jinjja":re.compile(r"이승환 콘서트 진짜"),
	"Star.has.2.Job":re.compile(r"스타는 투잡 중"),
	"Our.Home":re.compile(r"우리집"),
	"Love.Data":re.compile(r"러브데이터"),
	"Romance.of.the.Week":re.compile(r"로맨스의 일주일"),
	"Absolute.Man":re.compile(r"절대남자"),
	"Witch.and.Beast":re.compile(r"마녀와 야수"),
	"Network.Special.Choice":re.compile(r"네트워크특선"),
	"Comedy.Road":re.compile(r"코미디의 길"),
	"Marriage.Busters":re.compile(r"결혼 터는 남자들"),
	"Sisters.Choice":re.compile(r"언니들의 선택"),
	"Show.Champion":re.compile(r"쇼 챔피언"),
	"Stardust":re.compile(r"스타더스트 뮤비뱅크"),
	"I.See.Your.Voice":re.compile(r"너의\s*목소리가\s*보여"),
	"Problematic.Man":re.compile(r"문제적 남자"),
	"The.Secrets.of.Nature":re.compile(r"천기누설"),
	"Picnic.Live":re.compile(r"피크닉 라이브 소풍"),
	"Gagman.KimYoungCheols.Shameless.Travel.English.With.Deeva.Jessica":re.compile(r"개그맨 김영철의 뻔뻔한 여행영어 with 디바제시카\(Deeva Jessica\)"),
	"Match.Made.In.Heaven.Returns":re.compile(r"천생연분\.*\s*리턴즈"),
	"How.About.Tonight":re.compile(r"오늘밤 어때"),
	"Little.Big.Hero":re.compile(r"리틀빅 히어로"),
	"Delicious.Guys":re.compile(r"맛있는\s*녀석들"),
	"Sonamoos.Pet.House":re.compile(r"소나무의 펫하우스"),
	"One.Night.Study":re.compile(r"원나잇 스터디"),
	"Same.Bed.Different.Drama":re.compile(r"동상이몽\,*\s*괜찮아\s*괜찮아"),
	"Grandpas.over.Flowers":re.compile(r"꽃보다 할배"),
	"Show.Me.The.Money":re.compile(r"쇼미더머니"),
	"The.Girl.Who.Sees.Smell":re.compile(r"냄새를\s*보는\s*소녀"),
	"Crime.Scene":re.compile(r"크라임\s*씬"),
	"The.Bunker":re.compile(r"더 벙커"),
	# HDTV Feature
	"The.Hard.Goodbye":re.compile(r"내가 살았던 집"),
	"The.Post.Horse.Curse":re.compile(r"역마"),
	"The.Outdoor.Lamp":re.compile(r"외등"),
	"Sad.to.be.Forgotten":re.compile(r"서러워라\,* 잊혀진다는 것은"),
	"Saeya.Saeya":re.compile(r"새야새야"),
	"The.Buckwheat.Season":re.compile(r"메밀꽃\s*필\s*무렵"),
	"The.Last.Song":re.compile(r"노래여 마지막 노래여"),
	"Moon.Altar":re.compile(r"달의제단"),
	"Castella":re.compile(r"카스테라"),
	"My.Bloody.Valentine":re.compile(r"나의 피투성이 연인"),
	"Deungsinbul":re.compile(r"등신불"),
	"Sonaki":re.compile(r"소나기"),
	"Who.murdered.Kurt.Cobain":re.compile(r"누가 커트코베인을 죽였는가"),
	"Bad.Story":re.compile(r"나쁜소설"),
	"Way.To.Sampo":re.compile(r"삼포 가는 길"),
	}
