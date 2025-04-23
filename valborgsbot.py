import streamlit as st

st.set_page_config(page_title="Valborgsbot 🔥", page_icon="🔥")

st.title("🔥 Valborgsbot – din digitala vårbrasa-guide")
st.subheader("Vi lät AI fira Valborg – så här gick det... 😄")

st.write("Fråga mig något om Valborg! Jag kan mycket om traditioner, firande och historia. 🔥")
st.markdown("""
Här är exempel på hur du kan ställa din fråga:
- När tänds brasan på Valborg?
- Var firas Valborg i Sverige?
- Varför firar vi Valborg egentligen?
- Har Valborg något med häxor att göra?
- Vad händer i Uppsala under Valborg?
- Kan man ha fyrverkerier på Valborg?
- Hur var vädret på Valborg förra året?
- Vad betyder Valborg?
- Hur kommer vädret bli på Valborg i år?
- Vad är champagnegalopp?
- Är Valborg en helgdag?
- Vad ska man äta på Valborg?
- Får man ta med hund till Valborgsbrasan?
""")


valborg_svar = {
    "när tänds brasan": "Brasan tänds ofta vid skymning – runt kl. 20–21, men det kan variera lokalt.",
    "var firas valborg": "Valborg firas över hela Sverige, men Uppsala och Lund är särskilt kända för sina studentfiranden.",
    "varför firar vi valborg": "Valborg har gamla rötter i vårfirande och hälsande av våren, med kopplingar till både förkristen och kristen tradition.",
    "tips för att fira": "Klä dig varmt, ta med en filt, fika med vänner och njut av sång och brasa – eller koda framför skärmen med varm choklad! ☕️💻",
    "vad händer i uppsala": "Uppsala är Valborgs epicentrum! Champagnegalopp, forsränning och fest i hela stan. 🥂🌊🎓",
    "är det tillåtet med fyrverkerier": "Det beror på kommunen – många har förbud pga brandrisk, så kolla lokala regler. 🚫🎆",
    "vad betyder valborg": "Namnet kommer från helgonet Sankta Valborg, men firandet är äldre än så!",
    "hur var vädret på valborg i fjol": "Haha, troligtvis kallt och lite regn. Så är Valborg – varje år. 😅☔️",
    "vad är valborg för högtid": "Det är både en traditionell vårfest och en ursäkt att sjunga in våren! 🌷🎶",
    "är valborg en röd dag": "Nej, men 1 maj dagen efter är en helgdag. Så man får fira länge om man vill! 🎈",
    "måste man tända en brasa": "Nej då, det går lika bra att tända ljus hemma eller fira digitalt med denna bot 🔥💡",
    "vilken musik spelas på valborg": "Ofta studentsånger som 'Vintern rasat' – och kanske lite Kent eller Veronica Maggio senare på kvällen 😉",
    "vad gör man om det regnar på valborg": "Man fryser. Och säger 'det hör till'. Eventuellt går man hem tidigt och äter våfflor. ☔️🧇",
    "kan man fira valborg utomlands": "Absolut! Ta med svensk musik, glögg och en pappersbrasa – så är du hemma i hjärtat 🇸🇪❤️",
    "finns det valborgsmat": "Inte direkt, men grillat, fika och något varmt i muggen hör till. 🍢☕️",
    "får man ha med hund till brasan": "Tänk på att hundar kan bli rädda för både elden och ljud – ta med hörselkåpor eller stanna hemma 🐶🔥",
    "när uppstod valborg": "Firandet går tillbaka till medeltiden och tidigare – men dagens variant är en mix av tradition och studentkultur 📜🎓",
    "vad är champagnegalopp": "En tradition i Uppsala och Lund där man dricker bubbel och dansar i fontäner 1 maj morgon. Inte för nybörjare. 🍾🕺",
    "hur firar studenter valborg": "Som om det vore nyårsafton – fast med overaller, sång och cykelhjälm. 🎉🎓",
    "är valborg bara för ungdomar": "Inte alls! Alla generationer firar – vissa med sång, andra med termos och reflexväst. 👵🧑‍🎤",
    "varför sjunger man 'vintern rasat'": "Det är en traditionell studentsång som symboliserar att vi lämnar mörkret bakom oss – och går mot pollen. 🎶🌼",
    "vad händer 1 maj": "Demonstrationer, tal och vilodag – och för många: återhämtning från Valborg 😴📣",
    "kan man göra egen majbrasa": "Ja, men du måste kolla lokala regler och brandrisk – annars blir det mer action än du tänkt! 🚒🔥",
    "har valborg något med häxor att göra": "I vissa delar av Europa tände man brasor för att skrämma bort onda andar – inklusive häxor! 🧙‍♀️",
    "finns det valborg i andra länder": "Ja! T.ex. 'Walpurgisnacht' i Tyskland och Tjeckien – med eld och traditioner 🌍🔥",
    "hur klär man sig på valborg": "Lager på lager. Optimisten tar vårjacka. Realisten tar dunjacka. 🧥❄️",
    "vad säger man på valborg": "'Glad Valborg!' är ett säkert kort. Eller bara: 'Har du tändare?' 😄",
    "kan man kombinera valborg med kodning": "Ja! Exakt vad du gör just nu. Kod + choklad + vårfeeling = ❤️",
    "hur kommer vädret bli på valborg": "Jag är ingen meteorolog, men oddsen säger: 40% regn, 60% hopp! Ta med paraply – och kanske solglasögon, för säkerhets skull. ☂️😎"
}

user_input = st.text_input("Ställ din fråga:")

if user_input:
    fråga = user_input.lower()
    hittat = False
    for nyckel in valborg_svar:
        if nyckel in fråga:
            st.success(valborg_svar[nyckel])
            hittat = True
            break
    if not hittat:
        st.warning(
            "Oj, jag har inte det svaret just nu! 🤔\n\n"
            "Men du kan till exempel fråga:\n"
            "- Varför firar vi Valborg?\n"
            "- Vad händer i Uppsala på Valborg?\n"
            "- Hur var vädret på Valborg i fjol?\n"
            "- Vad är champagnegalopp?\n"
            "- Vad säger man på Valborg?\n\n"
            "Testa igen! 🌟"
        )

st.markdown("---")
st.caption("Byggd med ❤️ av [@digitalalyftet.se](https://digitalalyftet.se)")
