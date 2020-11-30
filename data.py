def sophie():
    image = "https://www.flaticon.com/svg/static/icons/svg/2358/2358252.svg"
    name = "sophie lee"
    github = "https://github.com/orgs/fruitycoders/people/sophieleeajh"

    return {"image": image, "name": name, "github": github}


def maggie():
    image = "https://www.flaticon.com/svg/static/icons/svg/2358/2358096.svg"
    name = "maggie killada"
    github = "https://github.com/orgs/fruitycoders/people/maggie3000"

    return {"image": image, "name": name, "github": github}


def adam():
    image = "https://www.flaticon.com/svg/static/icons/svg/2358/2358248.svg"
    name = "adam holbel"
    github = "https://github.com/orgs/fruitycoders/people/AdamHolbel"

    return {"image": image, "name": name, "github": github}


def linda():
    image = "https://www.flaticon.com/svg/static/icons/svg/2358/2358150.svg"
    name = "linda long"
    github = "https://github.com/orgs/fruitycoders/people/lindalonglong"

    return {"image": image, "name": name, "github": github}


def wenshi():
    image = "https://www.flaticon.com/svg/static/icons/svg/2358/2358323.svg"
    name = "wenshi bao"
    github = "https://github.com/orgs/fruitycoders/people/wenshibao"

    return {"image": image, "name": name, "github": github}


def persons():
    return [sophie(), maggie(), adam(), linda(), wenshi()]


def setup():
    title = "fruity photos"
    sophie = "https://github.com/sophieleeajh"
    linda = "https://github.com/lindalonglong"
    sophievid = "https://youtu.be/aPTJ5J0kxi0"
    lindavid = "https://www.youtube.com/watch?v=lu6bdBbVXh4"
    journal = "https://docs.google.com/spreadsheets/d/1elSgQhDFkBvTvTqnRh8zs0XKX0BS7Nr3QeHGaYTkk0k/edit?ouid=115921679004469073625&usp=sheets_home&ths=true"

    source = {"title": title, "sophie": sophie, "linda": linda, "sophievid": sophievid, "lindavid": lindavid,
              "journal": journal}

    return title

    project1 = "Hello Series"
    projlinks1 = [
        Link("Project Plan", ""),
        Link("Repl", ""),
    ]
    project2 = "Flask Project"
    projlinks2 = [
        Link("Project Plan", ""),
        Link("Repl", ""),
    ]

    proj1 = Project(project1, projlinks1)
    proj2 = Project(project2, projlinks2)

    projects = Projects(source, [proj1, proj2])
    return projects


class Link():
    def __init__(self, btn, href):
        self.btn = btn
        self.href = href

    def get_btn(self):
        return self.btn

    def get_href(self):
        return self.href


class Project():
    def __init__(self, name, links):
        self.name = name
        self.links = links

    def get_name(self):
        return self.name

    def get_links(self):
        return self.links


class Projects():
    def __init__(self, source, projects):
        self.source = source
        self.projects = projects

    def get_source(self):
        return self.source

    def get_projects(self):
        return self.projects
