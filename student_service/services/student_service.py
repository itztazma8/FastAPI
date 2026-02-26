from db_verification import connection

class StudentService:
    
    def create(self, student_list, conn):
        try:
            cursor=conn.cursor(dictionary=True)

            for student in student_list:

                query="INSERT INTO student_info (ID, First_Name, Last_Name, Semester) " \
                    "VALUES (%s, %s, %s, %s)"
                values=(student.id, student.first_name, student.last_name, student.semester)
    
                cursor.execute(query, values)
            conn.commit()

            return f"Table updated. Check database."
        except:
            print(f"Error Code: 201")
        finally:
            cursor.close()

    
    def fetch(self, student_id:int, conn):
        try:
            cursor=conn.cursor(dictionary=True)

            query="SELECT * FROM student_info WHERE ID=%s"
            value=(student_id,)

            cursor.execute(query, value)
            result=cursor.fetchall()

            return result
        except:
            print(f"Error Code: 200")
        finally:
            cursor.close()
        

        
    
    def delete(self, student_id:int, conn):
        try:
            cursor=conn.cursor(dictionary=True)

    
            query="DELETE FROM student_info WHERE ID=%s"
            value=(student_id,)
            cursor.execute(query,value)
    
            conn.commit()
            return f"Removed. Check Database."
        except:
            print(f"Error code: 204")
        finally:
            cursor.close()
        
    
    def update(self, student_id: int, data, conn):
        try:
            cursor=conn.cursor(dictionary=True)

            query="UPDATE student_info SET ID=%s, First_Name=%s, Last_Name=%s, Semester=%s " \
            "WHERE ID=%s"
            values=(data.id, data.first_name, data.last_name, data.semester, student_id)

            cursor.execute(query, values)
            conn.commit()
            return f"Updated Data. Check Database."
        except:
            print(f"Error Code 404")
        finally:
            cursor.close()
         

        
    
    def partial_update(self, student_id:int, data, conn):
        try:
            partial_data=data.dict(exclude_unset=True)

            if not partial_data:
                return f"No data found"
        
            cursor=conn.cursor(dictionary=True)

            for key,value in partial_data.items():
                query=f"UPDATE student_info SET {key}=%s WHERE ID=%s"
                items=(value, student_id)
                cursor.execute(query, items)
        
            conn.commit()
            return f"Data updated. Check Database!"
        except:
            print(f"Error Code: 404")
        finally:
            cursor.close()
        

        


