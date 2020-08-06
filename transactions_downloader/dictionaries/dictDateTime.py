class DictDatetime(object):

    @staticmethod
    def dict_moth(month):
        month = str(month)
        d = {}
        #   POLISH months
        d["01"] = "Styczeń"          # january
        d["02"] = "Luty"             # february
        d["03"] = "Marzec"           # march
        d["04"] = "Kwiecień"         # april
        d["05"] = "Maj"              # may
        d["06"] = "Czerwiec"         # june
        d["07"] = "Lipiec"           # july
        d["08"] = "Sierpień"         # august
        d["09"] = "Wrzesień"         # september
        d["10"] = "Październik"     # october
        d["11"] = "Listopad"        # november
        d["12"] = "Grudzień"        # december

        return(d[month])
