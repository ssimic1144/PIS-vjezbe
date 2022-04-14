from pony import orm

DB = orm.Database()

class Stvar(DB.Entity):
   stvar = orm.Required(str,unique=True)
   namjena = orm.Required(str)
   cijena = orm.Optional(float)

DB.bind(provider="sqlite", filename="database.sqlite", create_db=True)
DB.generate_mapping(create_tables=True)

def add_stvar(stvar,namjena,cijena=None):
    try:
        with orm.db_session:
            Stvar(stvar=stvar,namjena=namjena,cijena=cijena)
            response = {"response":"Success"}
            return response
    except Exception as e:
        return {"response":"Fail","error":e}


def get_stvar(stvar_to_get):
    try:
        with orm.db_session:
            #result = Stvar.get(stvar=stvar_to_get)
            result = orm.select(x for x in Stvar if x.stvar == stvar_to_get)[:][0]
            result = result.to_dict()
            response = {"response":"Success", "data":result}
            return response
    except Exception as e:
        return {"response":"Fail","error":e}

def patch_stvar(stvar_to_patch, cijena_to_patch):
    try:
        with orm.db_session:
            to_update = orm.select(x for x in Stvar if x.stvar == stvar_to_patch)[:][0]
            to_update.cijena = cijena_to_patch
            response = {"response":"Success"}
            return response
    except Exception as e:
        return {"response":"Fail","error":e}

def delete_stvar(stvar_to_delete):
    try:
        with orm.db_session:
            to_delete = orm.select(x for x in Stvar if x.stvar == stvar_to_delete)[:][0]
            to_delete.delete()
            response = {"response":"Success"}
            return response
    except Exception as e:
        return {"response":"Fail","error":e}


if __name__ == "__main__":
    res = add_stvar("lopta","igra",140)
    res = add_stvar("stol","igra")
    #print(res)
    res = get_stvar("stol")
    #print(res)
    res = patch_stvar("stol",11010)
    #print(res)
    res = get_stvar("stol")
    print(res)
    #res = delete_stvar("stol")
    #print(res)
    res = get_stvar("stol")
    print(res)


