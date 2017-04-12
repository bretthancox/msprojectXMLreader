import xmltodict
import pprint
import json
import datetime as dt

taskInfo = []
taskDict = {}
uidList = []
planXML = "Project_plan_04112017.xml"
jsonFromXml = "xmlToJson.txt"
assessmentFile = ("Project_parsed_{}.json".format(dt.date.today().strftime("%m_%d_%Y")))


with open(planXML) as fd:
    doc = xmltodict.parse(fd.read())

with open(jsonFromXml, 'w') as outjson:
    json.dump(doc, outjson)

with open(jsonFromXml, 'r') as injson:
    projectData = json.load(injson)


for i in range(0,1000):
    try:
        taskInfo.append({
            "UID": (projectData["Project"]["Tasks"]["Task"][i]["UID"]),
            "Name": (projectData["Project"]["Tasks"]["Task"][i]["Name"]),
            #"Start": ((projectData["Project"]["Tasks"]["Task"][i]["Start"])[0:10]),
            "StartDay": ((projectData["Project"]["Tasks"]["Task"][i]["Start"])[8:10]),
            "StartMonth": ((projectData["Project"]["Tasks"]["Task"][i]["Start"])[5:7]),
            "StartYear": ((projectData["Project"]["Tasks"]["Task"][i]["Start"])[0:4]),
            #"Finish": ((projectData["Project"]["Tasks"]["Task"][i]["Finish"])[0:10]),
            "FinishDay": ((projectData["Project"]["Tasks"]["Task"][i]["Finish"])[8:10]),
            "FinishMonth": ((projectData["Project"]["Tasks"]["Task"][i]["Finish"])[5:7]),
            "FinishYear": ((projectData["Project"]["Tasks"]["Task"][i]["Finish"])[0:4]),
            "Duration": (projectData["Project"]["Tasks"]["Task"][i]["DurationFormat"]),
            "Percent_complete": (projectData["Project"]["Tasks"]["Task"][i]["PercentComplete"]),
            })
    except IndexError:
        pass
    except KeyError:
        pass


with open(assessmentFile, 'w') as afRem:
    afRem.truncate()

with open(assessmentFile, 'a') as af:
    for j in range(0,1000):
        try:
            print(taskInfo[j])
            json.dump(taskInfo[j], af)
        except IndexError:
            pass
    
    
