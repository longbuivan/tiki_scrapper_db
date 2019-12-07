import yaml


class configObject:
    def __init__(self, save_path, website_path, page_number, dataframe):
        self.save_path = save_path
        self.website_path = website_path
        self.page_number = page_number
        self.dataframe = dataframe

    def save_path(self):
        return self.save_path

    def website_path(self):
        return self.website_path

    def page_number(self):
        return self.page_number
        
    def dataframe(self):
        return self.dataframe

with open("parse_config.yml", 'r') as ymlfile:
    cfg = yaml.load(ymlfile)
    for section in cfg:
        configObject.save_path = cfg['path']['save_path']
        configObject.website_path = cfg['path']['website_path']
        configObject.page_number = cfg['page']['page_number']
        configObject.dataframe = cfg['dataframe']

