from src.service.service_user import ServiceUser

class TestServiceUser:

    def test_add_user_success(self):
        name_add = 'Leonardo'
        job_add = 'TechLead'
        result_expect = 'Usuario adicionado com sucesso'
        service = ServiceUser()

        result = service.add_user(name=name_add, job=job_add)

        assert result_expect == result

    def test_validate_null_job(self):
        name_null = 'Matheus'
        job_null = None
        result_expect = 'Usuario nao adicionado'
        service = ServiceUser()

        result = service.add_user(name=name_null, job=job_null)

        assert result_expect == result

           
    def test_update_user(self):
        name_update = 'Joao'
        job_update = 'TI'
        result_expect = "Profissão atualizada com sucesso"
        service = ServiceUser()
        result = service.update_user(name=name_update, new_job=job_update)

        assert result_expect == result        


    def test_del_user_sucess(self):
        name_del = 'PO'
        result_expect = 'Usuario removido'
        service = ServiceUser()
        result = service.del_user(name=name_del)
        assert result_expect == result


    def test_select_user(self):
        name_check = 'Joao'
        result_expect = "Profissão: Ruim"
        service = ServiceUser()
        result = service.select_user(name_check)
        assert result_expect == result