from spyre import server
import pandas as pd

server.include_df_index = True



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
                    "options" : [{"label": "Vinnytska ", "value":1},
                           {"label": "Volinska ", "value":2},
                           {"label": "Dnipropetrovska ", "value":3},
                           {"label": "Donetska ", "value": 4},
                           {"label": "Zhytomyrska ", "value": 5},
                           {"label": "Zakarpattya ", "value": 6},
                           {"label": "Zaporizka ", "value": 7},
                           {"label": "Ivano-Frankivska ", "value": 8},
                           {"label": "Kyivska ", "value": 9},
                           {"label": "Kyrovohradska ", "value": 10},
                           {"label": "Luganska ", "value": 11},
                           {"label": "Lvivska ", "value": 12},
                           {"label": "Mykolaivska ", "value": 13},
                           {"label": "Odeska ", "value": 14},
                           {"label": "Poltavska ", "value": 15},
                           {"label": "Rivnenska ", "value": 16},
                           {"label": "Sumska ", "value": 17},
                           {"label": "Ternopilska ", "value": 18},
                           {"label": "Kharkyvska ", "value": 19},
                           {"label": "Khersonska ", "value": 20},
                           {"label": "Khmelnitska ", "value": 21},
                           {"label": "Cherkaska ", "value": 22},
                           {"label": "Chernivetska ", "value": 23},
                           {"label": "Chernihivska ", "value": 24},
                           {"label": "Crimean ", "value": 25}],
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