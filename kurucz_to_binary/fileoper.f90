      module file_operations

      implicit none

      public

      contains

      function num_of_lines(path_to_file) result(n)

      character (len = *), intent(in) :: path_to_file

      integer :: file_unit, n, io

      file_unit = 13745
     
      open(unit = file_unit, file = path_to_file, action = 'read')

      n = 0; io = 0

      do while (io == 0)

         read(file_unit, *, iostat = io)

         if (io .ne. 0) exit

         n = n + 1

      enddo

      close(file_unit)

      return

      end function

      end module
