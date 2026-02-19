from db_verification import connection

class StudentService:
    
    def create(self, student_list):
        conn=connection()
        cursor=conn.cursor(dictionary=True)

        for student in student_list:

            query="INSERT INTO student_info (ID, First_Name, Last_Name, Semester) " \
                "VALUES (%s, %s, %s, %s)"
            values=(student.id, student.first_name, student.last_name, student.semester)
    
            cursor.execute(query, values)
        conn.commit()

        cursor.close()
        conn.close()

        return f"Table updated. Check database."
    
    def fetch(self, student_id:int):
        conn=connection()
        cursor=conn.cursor(dictionary=True)

        query="SELECT * FROM student_info WHERE ID=%s"
        value=(student_id,)

        cursor.execute(query, value)
        result=cursor.fetchall()
        cursor.close()
        conn.close()

        return result
    
    def delete(self, student_id:int):
        conn=connection()
        cursor=conn.cursor(dictionary=True)

    
        query="DELETE FROM student_info WHERE ID=%s"
        value=(student_id,)
        cursor.execute(query,value)
    
        conn.commit()
        cursor.close()
        conn.close()

        return f"Removed. Check Database."
    
    def update(self, student_id: int, data):
        conn=connection()
        cursor=conn.cursor(dictionary=True)

        query="UPDATE student_info SET ID=%s, First_Name=%s, Last_Name=%s, Semester=%s " \
        "WHERE ID=%s"
        values=(data.id, data.first_name, data.last_name, data.semester, student_id)

        cursor.execute(query, values)
        conn.commit()
        cursor.close()
        conn.close() 

        return f"Updated Data. Check Database."
    
    def partial_update(self, student_id:int, data):
        partial_data=data.dict(exclude_unset=True)

        if not partial_data:
            return f"No data found"
        
        conn=connection()
        cursor=conn.cursor(dictionary=True)

        for key,value in partial_data.items():
            query=f"UPDATE student_info SET {key}=%s WHERE ID=%s"
            items=(value, student_id)
            cursor.execute(query, items)
        
        conn.commit()
        cursor.close()
        conn.close()

        return f"Data updated. Check Database!"


