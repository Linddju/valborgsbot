import streamlit as st

st.set_page_config(page_title="Valborgsbot 🔥", page_icon="🔥")

st.title("🔥 Valborgsbot – din digitala vårbrasa-guide")
st.subheader("Vi lät AI fira Valborg – så här gick det... 😄")

st.write("Fråga mig något om Valborg! Här är några exempel:")
st.markdown("- När tänds brasan?\n- Var firas Valborg?\n- Varför firar vi Valborg?\n- Tips för att fira?\n- Vad händer i Uppsala på Valborg?\n- Är det tillåtet med fyrverkerier?\n- Vad betyder Valborg?\n- Hur var vädret på Valborg i fjol?")

valborg_svar = {
    "när tänds brasan": "Brasan tänds ofta vid skymning – runt kl. 20–21, men det kan variera lokalt.",
    "var firas valborg": "Valborg firas över hela Sverige, men Uppsala och Lund är särskilt kända för sina studentfiranden.",
    "varför firar vi valborg": "Valborg har gamla rötter i vårfirande och hälsande av våren, med kopplingar till både förkristen och kristen tradition.",
    "tips för att fira": "Klä dig varmt, ta med en filt, fika med vänner och njut av sång och brasa – eller koda framför skärmen med varm choklad! ☕️💻",
    "vad händer i uppsala": "Uppsala är Valborgs epicentrum! Champagnegalopp, forsränning och fest i hela stan. 🥂🌊🎓",
    "är det tillåtet med fyrverkerier": "Det beror på kommunen – många har förbud pga brandrisk, så kolla lokala regler. 🚫🎆",
    "vad betyder valborg": "Namnet kommer från helgonet Sankta Valborg, men firandet är äldre än så!",
    "hur var vädret på valborg i fjol": "Haha, troligtvis kallt och lite regn. Så är Valborg – varje år. 😅☔️"
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
        st.info("Jag vet inte riktigt... kanske är det något bara våren själv kan svara på. 🌸")

st.markdown("---")
st.caption("Byggd med ❤️ av [@digitalalyftet.se](https://digitalalyftet.se)")
