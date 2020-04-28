from spyre import server
import pandas as pd

server.include_df_index = True
#новий коментар для перевірки
#новий коментра від нової вітки


class MyApp(server.App):
    title = "myappfirst"

    inputs = [ {    "type": 'dropdown',
                    "label": 'write year',
                    "options": [{'label': str(i), 'value': i} for i in range(1982, 2020)],
                    'key': 'year',
                    'value': '1982'},
                {
                    "type":'dropdown',
                    "label": 'write province',
                    "options" : [{"label": "Vinnytska province", "value":1},
                           {"label": "Volinska province", "value":2},
                           {"label": "Dnipropetrovska province", "value":3},
                           {"label": "Donetska province", "value": 4},
                           {"label": "Zhytomyrska province", "value": 5},
                           {"label": "Zakarpattya province", "value": 6},
                           {"label": "Zaporizka province", "value": 7},
                           {"label": "Ivano-Frankivska province", "value": 8},
                           {"label": "Kyivska province", "value": 9},
                           {"label": "Kyrovohradska province", "value": 10},
                           {"label": "Luganska province", "value": 11},
                           {"label": "Lvivska province", "value": 12},
                           {"label": "Mykolaivska province", "value": 13},
                           {"label": "Odeska province", "value": 14},
                           {"label": "Poltavska province", "value": 15},
                           {"label": "Rivnenska province", "value": 16},
                           {"label": "Sumska province", "value": 17},
                           {"label": "Ternopilska province", "value": 18},
                           {"label": "Kharkyvska province", "value": 19},
                           {"label": "Khersonska province", "value": 20},
                           {"label": "Khmelnitska province", "value": 21},
                           {"label": "Cherkaska province", "value": 22},
                           {"label": "Chernivetska province", "value": 23},
                           {"label": "Chernihivska province", "value": 24},
                           {"label": "Crimean province", "value": 25}],
                    "key": 'province'
                },
                {
                    "type" : 'text',
                    "key" : 'min',
                    "label" : 'min week',
                    'value': '1'
                },
                {
                    "type" : 'text',
                    "key" : 'max',
                    "label" : 'max week',
                    'value': '52'
                }
                    
            ]

    outputs = [ {  'type': 'table',
                    'id': 'table1',
                    'control_id': 'ok',
                    'tab': 'table1'
            
                    },
                {   'type': 'plot',
                    'id': 'plot1',
                    'control_id': 'ok',
                    'tab': 'plot1'},
                    {  'type': 'table',
                    'id': 'table2',
                    'control_id': 'ok',
                    'tab': 'table2'
                    },
                     {'type': 'plot',
                    'id': 'plot2',
                    'control_id': 'ok',
                    'tab': 'plot2'} ]

    controls = [{   "type": 'button',
                    'id': 'ok',
                    'label': 'ok'   }]

    tabs = ["plot1", "table1","table2","plot2"]

    def table1(self, params):
        name ='vhi_{}.csv'
        df = pd.DataFrame()
        year = int(params['year'])
        minweek = int(params['min'])       
        maxweek = int(params['max']) 
        province = int(params['province'])
        temp = pd.read_csv(name.format(province), sep='[, ]+', engine='python')
        df = df.append(temp, ignore_index=True)
        frame = df[(df['year'] == year) & (df['week'] >= minweek) & (df['week'] <= maxweek)][['year', 'week', 'VHI', 'TCI', 'VCI']]
        return frame

    def plot1(self, params):
        f1 = self.table1(params)
        frame = f1[['VCI', 'TCI', 'VHI']]
        return frame.set_index(f1['week']).plot()
        
    def table2(self, params):
        name ='vhi_{}.csv'
        df = pd.DataFrame()
        minweek = int(params['min'])       
        maxweek = int(params['max']) 
        province = int(params['province'])
        temp = pd.read_csv(name.format(province), sep='[, ]+', engine='python')
        df = df.append(temp, ignore_index=True)
        frame = df[(df['week'] >= minweek) & (df['week'] <= maxweek)][['week','VHI']]
        fr1 = frame.groupby(['week'])
        return fr1
    
    def plot2(self, params):
        fr = self.table2(params)
        return fr.plot()
   
app = MyApp()
app.launch( )