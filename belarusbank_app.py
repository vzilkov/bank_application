# importing the requests library
import requests
import json

from bs4 import BeautifulSoup

class belarusbank_class:
    def __init__(self):
        self.URL = "https://belarusbank.by/api/kursExchange?city=Орша"
        self.CITY = "Орша"
        self.pln_in_max = 0
        self.pln_out_max = 0

    def get_json_response(self):
        response = requests.get(url= self.URL)
        response_json = response.json()

        return response_json
    
    def get_actual_offices_for_pln(self, json_var):
        
        for line in json_var:
            pln_in = float(line['PLN_in'])
            pln_out = float(line['PLN_out'])
            if pln_in and pln_out:
                print(f"{pln_in=} {pln_out=} {line['name']} {line['street']} {line['home_number']}")
            if self.pln_in_max < pln_in:
                self.pln_in_max = pln_in
            if self.pln_out_max < pln_out:
                self.pln_out_max = pln_out
#"USD_in":"3.2100","USD_out":"3.2500","EUR_in":"3.4100","EUR_out"
    def get_max_vals(self):
        self.get_actual_offices_for_pln(self.get_json_response())
        x = dict(pln_in_max = self.pln_in_max, pln_out_max = self.pln_out_max)
        return x

class pkoBP_class:
    def __init__(self):
        print("PKO class inited")
        self.kantor_url = 'https://www.pkobp.pl/kantor-internetowy-kursy/'

    def get_http_pkobp(self):
        rawResponse = requests.get(url=self.kantor_url)
        # jsonResponse = rawResponse.json()
        soupResponse = BeautifulSoup(rawResponse.text, "html.parser")
        table_cantor_table = soupResponse.find_all("table", {"class": "table-cantor"})
        table_cantor_table = soupResponse.find('table', class_= 'table-cantor')
        for row in table_cantor_table.tbody.find_all('tr'):
            for column in row.find_all('td'):
                print(column)
         # <table class="table-cantor"><caption><span class="table-cantor__text-grey">Kursy wymiany z: 05.05.2024;</span> 21:38**
        
    # </caption><thead><tr><th><span class="table-cantor__text-grey">Kursy wymiany z: 05.05.2024;</span> 21:38**
            
    #     </th><th>Kupno</th><th>Sprzedaż</th></tr></thead><tbody><tr><td><span class="course__flag"><svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" id="svg10360" viewBox="0 0 810 426"><desc id="desc10362">European flag</desc><defs id="defs10364"><g id="1010101s"><g id="1010101c"><path transform="rotate(18 3.157 -.5)" d="M0 0v1h.5z" id="1010101t"></path><use height="100%" width="100%" id="use10369" transform="scale(-1 1)" xlink:href="#1010101t"></use></g><g id="1010101a"><use height="100%" width="100%" id="use10372" transform="rotate(72)" xlink:href="#1010101c"></use><use height="100%" width="100%" id="use10374" transform="rotate(144)" xlink:href="#1010101c"></use></g><use height="100%" width="100%" id="use10376" transform="scale(-1 1)" xlink:href="#1010101a"></use></g></defs><path id="rect10378" fill="#039" d="M0 0h810v426H0z"></path><g id="g10380" transform="translate(405 215.042) scale(21.3789)" fill="#fc0"><use height="100%" width="100%" id="use10382" y="-6" xlink:href="#1010101s"></use><use height="100%" width="100%" id="use10384" y="6" xlink:href="#1010101s"></use><g id="1010101l"><use height="100%" width="100%" id="use10387" x="-6" xlink:href="#1010101s"></use><use height="100%" width="100%" id="use10389" transform="rotate(-144 -2.344 -2.11)" xlink:href="#1010101s"></use><use height="100%" width="100%" id="use10391" transform="rotate(144 -2.11 -2.344)" xlink:href="#1010101s"></use><use height="100%" width="100%" id="use10393" transform="rotate(72 -4.663 -2.076)" xlink:href="#1010101s"></use><use height="100%" width="100%" id="use10395" transform="rotate(72 -5.076 .534)" xlink:href="#1010101s"></use></g><use height="100%" width="100%" id="use10397" transform="scale(-1 1)" xlink:href="#1010101l"></use></g></svg>
    #                     EUR
                        
                    
    #             </span></td><td>4,2887 <span class="table-cantor__text-grey">PLN</span></td><td>4,3651 <span class="table-cantor__text-grey">PLN</span></td></tr><tr><td><span class="course__flag"><svg xmlns="http://www.w3.org/2000/svg" id="svg7012" viewBox="0 0 320 168"><path id="rect7014" fill="#d52b1e" d="M0 0h320v168H0z"></path><path id="rect7016" fill="#fff" d="M107.5 68.25h105v31.5h-105z"></path><path id="rect7018" fill="#fff" d="M144.25 31.5h31.5v105h-31.5z"></path></svg>
    #                     CHF
                        
                    
    #             </span></td><td>4,3852 <span class="table-cantor__text-grey">PLN</span></td><td>4,4927 <span class="table-cantor__text-grey">PLN</span></td></tr><tr><td><span class="course__flag"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 473" version="1"><path fill="#d7141a" d="M0 .089h898.703V473H0z"></path><path fill="#f0f0f0" d="M0 .089h898.703v236.455H0z"></path><path d="M354.683 236.545L0 .089V473z" fill="#11457e"></path></svg>

    #                     CZK
                        
                    
    #             </span></td><td>0,1702 <span class="table-cantor__text-grey">PLN</span></td><td>0,1755 <span class="table-cantor__text-grey">PLN</span></td></tr><tr><td><span class="course__flag"><svg xmlns="http://www.w3.org/2000/svg" id="svg15296" viewBox="0 0 1100 578"><path id="rect15298" fill="#ef2b2d" d="M0 3.455h1100V578H0z"></path><path id="rect15300" fill="#fff" d="M216.75 0h144.5v578h-144.5z"></path><path id="rect15302" fill="#fff" d="M0 216.75h1100v144.5H0z"></path><path id="rect15304" fill="#002868" d="M252.875 0h72.25v578h-72.25z"></path><path id="rect15306" fill="#002868" d="M0 252.875h1100v72.25H0z"></path></svg>
    #                     NOK
                        
                    
    #             </span></td><td>0,3635 <span class="table-cantor__text-grey">PLN</span></td><td>0,3767 <span class="table-cantor__text-grey">PLN</span></td></tr><tr><td><span class="course__flag"><svg xmlns="http://www.w3.org/2000/svg" id="svg9245" viewBox="0 0 370 195"><path id="rect9247" fill="#c60c30" d="M0 0h370v195H0z"></path><path id="rect9249" fill="#fff" d="M120 0h40v195h-40z"></path><path id="rect9251" fill="#fff" d="M0 83.571h370v27.857H0z"></path></svg>
    #                     DKK
                        
                    
    #             </span></td><td>0,5734 <span class="table-cantor__text-grey">PLN</span></td><td>0,5868 <span class="table-cantor__text-grey">PLN</span></td></tr><tr><td><span class="course__flag"><svg xmlns="http://www.w3.org/2000/svg" id="svg18114" viewBox="0 0 16 8.42"><path id="rect18116" fill="#006aa7" d="M0 0h16v8.42H0z"></path><path id="rect18118" fill="#fecc00" d="M4.21 0h1.684v8.42H4.21z"></path><path id="rect18120" fill="#fecc00" d="M0 3.368h16v1.684H0z"></path></svg>
    #                     SEK
                        
                    
    #             </span></td><td>0,3652 <span class="table-cantor__text-grey">PLN</span></td><td>0,3785 <span class="table-cantor__text-grey">PLN</span></td></tr><tr><td><span class="course__flag"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 60 31.6"><path fill="#00247d" class="flag-en__blue" d="M0 0h60v31.6H0z"></path><path d="M1.475-2.656L-1.383 2.78 23.398 15.8l-24.78 13.02 2.857 5.435L30 19.27l28.525 14.986 2.858-5.435L36.602 15.8l24.78-13.02-2.857-5.437L30 12.332 1.475-2.656z" fill="#fff"></path><path d="M.15.1l29.854 15.685V13.44L4.616.1H.15zm29.854 15.685h4.466L59.95 2.398V.1h-.091L30.003 15.785zm0 0v2.347L55.45 31.5h4.466l-29.91-15.715zm0 0H25.54L.05 29.177V31.5h.044l29.91-15.715z" class="flag-en__red" fill="#cf142b"></path><path d="M24.883.062V10.68H.045v10.236h24.838v10.621h10.234v-10.62h24.838V10.68H35.117V.06H24.883z" fill="#fff"></path><path d="M26.93.062V12.73H.045v6.14H26.93v12.668h6.14V18.87h26.885v-6.14H33.07V.062h-6.14z" fill="#cf142b" class="flag-en__red"></path></svg>
    #                     GBP
                        
                    
    #             </span></td><td>4,9897 <span class="table-cantor__text-grey">PLN</span></td><td>5,0989 <span class="table-cantor__text-grey">PLN</span></td></tr><tr><td><span class="course__flag"><svg xmlns="http://www.w3.org/2000/svg" id="svg13631" viewBox="0 0 6 3.16"><path id="rect13633" fill="#436f4d" d="M0 0h6v3.16H0z"></path><path id="rect13635" fill="#fff" d="M0 0h6v2.107H0z"></path><path id="rect13637" fill="#cd2a3e" d="M0 0h6v1.053H0z"></path></svg>
    #                     HUF
                        
    #                     *
                        
                    
    #             </span></td><td>1,0924 <span class="table-cantor__text-grey">PLN</span></td><td>1,1306 <span class="table-cantor__text-grey">PLN</span></td></tr><tr><td><span class="course__flag"><svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 7410 3900"><path fill="#b22234" d="M0 0h7410v3900H0z"></path><path d="M0 450h7410m0 600H0m0 600h7410m0 600H0m0 600h7410m0 600H0" stroke="#fff" stroke-width="300"></path><path fill="#3c3b6e" d="M0 0h2964v2100H0z"></path><g fill="#fff"><g id="s18"><g id="s9"><g id="s5"><g id="s4"><path id="s" d="M247 90l70.534 217.082-184.66-134.164h228.253L176.466 307.082z"></path><use xlink:href="#s" y="420"></use><use xlink:href="#s" y="840"></use><use xlink:href="#s" y="1260"></use></g><use xlink:href="#s" y="1680"></use></g><use xlink:href="#s4" x="247" y="210"></use></g><use xlink:href="#s9" x="494"></use></g><use xlink:href="#s18" x="988"></use><use xlink:href="#s9" x="1976"></use><use xlink:href="#s5" x="2470"></use></g></svg>
    #                     USD
                        
                    
    #             </span></td><td>3,9702 <span class="table-cantor__text-grey">PLN</span></td><td>4,0682 <span class="table-cantor__text-grey">PLN</span></td></tr></tbody></table>
        return rawResponse


# belbank = belarusbank_class()
# response = belbank.get_max_vals()
# print(f"{response['pln_in_max']=} {response['pln_out_max']=}")

pko_val = pkoBP_class()
pko_val.get_http_pkobp()
