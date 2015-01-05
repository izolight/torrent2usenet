#! /usr/bin/python3
import re,shutil,os,sys

TMP_DIR = '/home/***REMOVED***/post_to_usenet/'
RUNNING = 't2u.running'

if (os.path.isfile(TMP_DIR + RUNNING)):
	print('script already running, exiting')
	sys.exit()

os.system('touch ' + TMP_DIR + RUNNING)

directory = os.listdir(TMP_DIR)

#Hangul to English matching
names = {
	#drama
	"Mr.Back":re.compile(r"미스터 백"),
	"Pinocchio":re.compile(r"피노키오"),
	"The.Kings.Face":re.compile(r"왕의 얼굴"),
	"Cheongdamdong.Scandal":re.compile(r"청담동 스캔들"),
	"Make.a.Wish":re.compile(r"소원을 말해봐"),
	"Lady.of.the.Storm":re.compile(r"폭풍의 여자"),
	"Healer":re.compile(r"힐러"),
	"Family.Secrets":re.compile(r"가족의 비밀"),
	"Punch":re.compile(r"펀치"),
	"Sunam.Girls.High.School.Detectives":re.compile(r"선암여고 탐정단"),
	"Valid.Love":re.compile(r"일리있는 사랑"),
	"Pride.and.Prejudice":re.compile(r"오만과 편견"),
	"Tears.of.Heaven":re.compile(r"천국의 눈물"),
	"What.happens.to.my.Family":re.compile(r"가족끼리 왜 이래"),
	"Rosy.Lovers":re.compile(r"장미빛 연인들"),
	"The.legend.of.the.Witch":re.compile(r"전설의 마녀"),
	"Dr.Frost":re.compile(r"닥터 프로스트"),
#	"Misaeng":re.compile(r"미생"),	
	"Misaengmul":re.compile(r"미생물"),
	"Birth.of.a.Beauty":re.compile(r"미녀의 탄생"),
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
	#ent
	"Superstar.K6.B-Side":re.compile(r"슈퍼스타K 6 B-SIDE"),
	"Hello.Stranger":re.compile(r"헬로 이방인"),
	"Happy.Together":re.compile(r"해피\s*투게더"),
	"Oh.My.Baby":re.compile(r"오(\!)* 마이 베이비"),
	"Witch.Hunt":re.compile(r"마녀사냥"),
	"Infinity.Challenge":re.compile(r"무한도전"),
	"We.Got.Married":re.compile(r"우리\s*결혼했어요"),
	"Music.Core":re.compile(r"쇼! 음악중심"),
	"3.Meals.a.Day":re.compile(r"삼시세끼"),
	"Star.Married.Couple":re.compile(r"자기야 백년손님"),
	"A.very.curious.story":re.compile(r"아궁이"),
	"Cook.King.Korea":re.compile(r"쿡킹 코리아"),
	"World.Changing.Quiz":re.compile(r"세바퀴"),
	"Super.Idol.Chartshow":re.compile(r"슈퍼 아이돌 차트쇼"),
	"Song.Festival":re.compile(r"가요대축제"),
	"Entertainment.Awards":re.compile(r"연예대상"),
	"Always.Cantare":re.compile(r"언제나 칸타레"),
	"Cartalk.Show.S.":re.compile(r"카톡쇼 S"),
	"My.Bodys.Usage.Manual":re.compile(r"내 몸 사용 설명서"),
	"Lets.go.to.School":re.compile(r"학교 다녀오겠습니다"),
	"Love.Unification.of.South.Man.and.North.Women":re.compile(r"애정통일 남남북녀"),
	"My.young.Tutor":re.compile(r"띠동갑내기 과외하기"),
	"Law.of.the.Jungle.in.Costa.Rica":re.compile(r"정글의 법칙 in 코스타리카"),
	"Inkigayo":re.compile(r"인기가요"),
	"Star.King":re.compile(r"놀라운 대회 스타킹"),
	"Actresses.Secret.Travel.in":re.compile(r"여우비행 인"),
	"Good.Sunday.K-Pop.Star":re.compile(r"(일요일이 좋다-)*K팝스타"),
	"Good.Sunday.Running.Man":re.compile(r"(일요일이 좋다\s*-\s*)*런닝맨"),
	"Good.Sunday.Survival.Audition.K-Pop.Star":re.compile(r"일요일이 좋다-서바이벌 오디션 K팝스타"),
	"The.Return.of.Superman":re.compile(r"슈퍼맨이 돌아왔다"),
	"Our.Sunday.Night.Daddy.Where.Are.You.Going":re.compile(r"(일밤 1부 )*아빠\!* 어디가"),
	"Our.Sunday.Night.Real.Man":re.compile(r"일밤 2부 진짜 사나이"),
	"Saturday.Freedom.Immortal.Music":re.compile(r"불후의 명곡 전설을 노래하다"),
	"Happy.Sunday.2Days.1Night":re.compile(r"해피 선데이 - 1박2일"),
	"Comedy.Big.League":re.compile(r"코미디 빅리그"),
	"Smile.People":re.compile(r"웃음을 찾는 사람들"),
	"Gag.Concert":re.compile(r"개그콘서트"),
	"I.Live.Alone":re.compile(r"나 혼자 산다"),
	"SuperJuniorM.Guest.House":re.compile(r"슈퍼주니어M 게스트하우스"),
	"Lets.Go.Dream.Team":re.compile(r"출발 드림팀"),
	"Extreme.Surprise":re.compile(r"익스트림 서프라이즈"),
	"Mysterious.TV.Surprise":re.compile(r"신비한TV 서프라이즈"),
	"Concert.7080":re.compile(r"배철수의 콘서트 7080"),
	"Salon.de.raison":re.compile(r"속사정쌀롱"),
	"Take.Care.of.the.Fridge":re.compile(r"냉장고를 부탁해"),
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
	"2Days.1Night":re.compile(r"1박2일"),
	"Marriage.Talk":re.compile(r"결혼 이야기"),
	"Sseol.Jeon":re.compile(r"썰전"),
	"Power.to.Children":re.compile(r"아이에게 권력을"),
	"I.have.a.Gods.Body":re.compile(r"나는 몸신이다( 베스트)*"),
	"Capture.the.Moment.How.is.that.possible":re.compile(r"순간포착 세상에 이런일이"),
	"Music.Bank":re.compile(r"뮤직뱅크"),
	"YooHeeYeols.Sketchbook":re.compile(r"유희열의 스케치북"),
	"Talk.with.Star.in.Taxi":re.compile(r"현장토크쇼 택시"),
	"Laws.of.the.Jungle":re.compile(r"정글의 법칙"),
	"Future.Predictions.Variety.Butterfly.Effect":re.compile(r"미래예측 버라이어티 나비효과"),
	"Sweden.Laundry":re.compile(r"스웨덴 세탁소"),
	"Show.Music.Core":re.compile(r"쇼\! 음악중심"),
	"I.love.Movie":re.compile(r"영화가 좋다"),
	"Movieworld":re.compile(r"접속! 무비월드"),
	"Entertainment.Weekly":re.compile(r"연예가\s*중계"),
	"The.Human.Condition":re.compile(r"인간의 조건"),
	"Start.Video.Tour":re.compile(r"출발! 비디오 여행"),
	"Star.Junior.Show":re.compile(r"스타주니어쇼 붕어빵"),
	"TV.Zoo":re.compile(r"TV 동물농장"),
	"Find.Delicious.TV":re.compile(r"찾아라! 맛있는 TV"),
	"Vienna.Philharmonic.Orchestra.New.Years.Concert":re.compile(r"비엔나 필하모닉 오케스트라 신년음악회"),
	"Section.TV":re.compile(r"섹션TV 연예통신"),
	"Gourmet.Road":re.compile(r"식신로드"),
	}

for filename in directory:
	if (os.path.isdir(filename)):
		continue
	for key in names:
		if (re.search(names[key],filename)):
			#print('processing %s' % filename)
			# preprocessing
#			print("removing tags from: %s" % filename)
			new_filename = re.sub(r"\[.*\]\s*","",filename)
#			print("removing 내정보releasename from: %s" % new_filename)
			new_filename = re.sub(r"\.내정보","",new_filename)
			# convert to english
#			print("converting %s to english" % new_filename)
			new_filename = re.sub(names[key],key,new_filename)
			# remove whitespace
#			print("replacing whitespace with dots in %s" % new_filename)
			new_filename = re.sub(r"\s",".",new_filename)
			# part 1,2,3 etc
#			print("replacing 부with Part in %s" % new_filename)
			new_filename = re.sub(r"부","Part",new_filename)			
			new_filename = re.sub(r"시즌", "Season", new_filename)
			new_filename = re.sub(r"신년특집", "New.Year.Special", new_filename)
#			print("renaming %s to %s" % (filename,new_filename))
			os.rename(TMP_DIR + filename, TMP_DIR + new_filename) # rename hangul to korean
			foldername = new_filename[:-4]
#			print("making folder %s" % foldername)
			os.mkdir(TMP_DIR + foldername) # make folder without file ending			
			shutil.move(TMP_DIR + new_filename, TMP_DIR + foldername) # move file to folder
#			print("calling rarnpar on %s" % foldername)
			os.system("rarnpar -N -D " + TMP_DIR + foldername) # rar n par
			os.remove(TMP_DIR + foldername + "/" + new_filename) # remove video
			os.system("GoPostStuff -d "+ TMP_DIR + foldername) # post rar n pars
			shutil.rmtree(TMP_DIR + foldername) # remove files						

os.remove(TMP_DIR + RUNNING)
sys.exit()
