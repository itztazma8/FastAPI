from mysql.connector import Error, IntegrityError
from fastapi import HTTPException, status


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
        except IntegrityError:
            conn.rollback()
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Duplicate ID"
            )
        except Exception as e:
            conn.rollback()
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=str(e)
            )
        finally:
            cursor.close()

    def fetch_all(self, conn, skip, limit):
        try:
            cursor=conn.cursor(dictionary=True)
            query = f"SELECT * FROM student_info LIMIT {int(limit)} OFFSET {int(skip)}"
            cursor.execute(query)
            result = cursor.fetchall()
            return result

        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                                detail=str(e))
        
        finally:
            cursor.close()

    def fetch(self, student_id:int, conn):
        try:
            cursor=conn.cursor(dictionary=True)

            query="SELECT * FROM student_info WHERE ID=%s"
            value=(student_id,)

            cursor.execute(query, value)
            result=cursor.fetchone()

            if not result:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                    detail="No Details Found")
            return result
        
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                                detail=str(e))
        finally:
            cursor.close()
        

    def delete(self, student_id:int, conn):
        try:
            cursor=conn.cursor(dictionary=True)

            query="SELECT * FROM student_info WHERE ID=%s"
            value=(student_id,)
            cursor.execute(query, value)
            result=cursor.fetchone()
            
            if not result:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                    detail="No ID found")
            
            query="DELETE FROM student_info WHERE ID=%s"
            value=(student_id,)
            cursor.execute(query,value)
    
            conn.commit()
            return f"Removed. Check Database."
        except Exception as e:
            conn.rollback()
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                                detail=str(e))
        finally:
            cursor.close()
        
    
    def update(self, student_id: int, data, conn):
        try:
            cursor=conn.cursor(dictionary=True)

            query="SELECT * FROM student_info WHERE ID=%s"
            values=(student_id,)
            cursor.execute(query, values)
            result=cursor.fetchone()
            
            if not result:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                    detail="ID does not exist")
            
            query="UPDATE student_info SET ID=%s, First_Name=%s, Last_Name=%s, Semester=%s " \
            "WHERE ID=%s"
            values=(data.id, data.first_name, data.last_name, data.semester, student_id)

            cursor.execute(query, values)
            conn.commit()
            return f"Updated Data. Check Database."
        
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                                detail=str(e))
        finally:
            cursor.close()
         

    
    def partial_update(self, student_id:int, data, conn):
        try:
            partial_data=data.dict(exclude_unset=True)

            if not partial_data:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                                    detail="No data found")
            

            cursor=conn.cursor(dictionary=True)

            query="SELECT * FROM student_info WHERE ID=%s"
            values=(student_id,)
            cursor.execute(query, values)
            result=cursor.fetchone()

            if not result:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                    detail="No ID found")
            
            for key,value in partial_data.items():
                query=f"UPDATE student_info SET {key}=%s WHERE ID=%s"
                items=(value, student_id)
                cursor.execute(query, items)
        
            conn.commit()
            return f"Data updated. Check Database!"
        
        except Exception as e:
            conn.rollback()
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                                detail=str(e))
        finally:
            cursor.close()
        

        


