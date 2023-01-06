      program repack

      use file_operations

      implicit none

      double precision, allocatable, dimension(:) :: wvl, atst, gf, E_low, E_up, gr, gs, gw

      double precision, allocatable, dimension(:) :: v5, v7

      integer, allocatable, dimension(:) :: v11

      character(len = 80) :: ldat, lbin

!      integer(kind = 4) :: n_lines, l, block_size, n_blocks, n_rem_lin, m, i, nl, e, s, j
      integer(kind = 4) :: n_lines, l, block_size, n_blocks, m, i, nl, e, s, j

      integer(kind = 4) :: pack1(4, 2000)
      integer(kind = 2) :: pack2(8, 2000)

      integer (kind = 4) :: idx
      integer (kind = 2) :: ic, lic

      equivalence (pack1(1, 1), pack2(1, 1))

!      ldat = 'vald_kurucz_merged.dat'
!      lbin = 'vald_kurucz_merged.bin'
      ldat = 'vald_in_kurucz_format.dat'
      lbin = 'vald.bin'

!      n_lines = num_of_lines('Kurucz_comb_air_8.97670nm_to_10000nm.dat')
!      n_lines = num_of_lines('vald_in_kurucz_format.dat')
      n_lines = num_of_lines(ldat)

      print*, 'n_lines = ', n_lines

      allocate(wvl(n_lines))
      allocate(atst(n_lines))
      allocate(gf(n_lines))
      allocate(E_low(n_lines))
      allocate(E_up(n_lines))
      allocate(gr(n_lines))
      allocate(gs(n_lines))
      allocate(gw(n_lines))

      allocate(v5(n_lines))
      allocate(v7(n_lines))
      allocate(v11(n_lines))

!      open(unit = 1, file = 'Kurucz_comb_air_8.97670nm_to_10000nm.dat', action = 'read')
!      open(unit = 1, file = 'vald_in_kurucz_format.dat', action = 'read')
      open(unit = 1, file = ldat, action = 'read')

      print*, 'Reading the lines...'

      read(1, *) (wvl(l), atst(l), gf(l), E_low(l), v5(l), E_up(l), v7(l), gr(l), gs(l), gw(l), v11(l), l = 1, n_lines)

      close(1)

      print*, 'Writing the lines...'

      open(unit = 2, file = lbin, type = 'new', form = 'unformatted', recordtype = 'fixed', blocksize = 32000, recl = 8000)

      block_size = 2000

      n_blocks = n_lines / block_size

!      n_rem_lin = n_lines - n_blocks * block_size

      pack1(:, :) = 0
      pack2(:, :) = 0

      l = 0
      m = 0
      j = 0

      do i = 1, n_lines

         e = floor(atst(i))

         if (e .ne. 1) then

             j = j + 1

             l = l + 1

             pack1(1, l) = idx(wvl(i))

             s = int((atst(i) - e) * 100, 4)

             pack2(3, l) = (e - 1) * 6 + s + 1

             pack2(4, l) = lic(E_low(i))

             pack2(5, l) = ic(gf(i))

             pack2(6, l) = ic(gr(i))

             pack2(7, l) = ic(gs(i))

             pack2(8, l) = ic(gw(i))

             if (lic(E_low(i)) <= 1.0) write(*, '(A,2(1x,I9),2(1x,f7.3))'), 'E_low', i, lic(E_low(i)), E_low(i), gf(i)
             if (ic(gf(i))     <= 1.0) write(*, '(A,2(1x,I9),  1x,f7.3)'),  'gf',    i, ic(gf(i)),     gf(i)
             if (ic(gr(i))     <= 1.0) write(*, '(A,2(1x,I9),2(1x,f7.3))'), 'gr',    i, ic(gr(i)),     gr(i), gf(i)
             if (ic(gs(i))     <= 1.0) write(*, '(A,2(1x,I9),2(1x,f7.3))'), 'gs',    i, ic(gs(i)),     gs(i), gf(i)
             if (ic(gw(i))     <= 1.0) write(*, '(A,2(1x,I9),2(1x,f7.3))'), 'gw',    i, ic(gw(i)),     gw(i), gf(i)

             if (l .eq. block_size .or. i .eq. n_lines) then

                m = m + 1

!                print*, m, ' blocks written...'

!                if (i .eq. n_lines .and. n_rem_lin .ne. 0) pack1(:, n_rem_lin + 1 : 2000) = 0

                write(2) pack1

                pack1(:, :) = 0
                pack2(:, :) = 0

                l = 0

             endif

         endif

      enddo

      close(2)

      print*, 'Number of non-H lines is ', j

      deallocate(wvl, atst, gf, E_low, E_up, gr, gs, gw)

      deallocate(v5, v7, v11)

      end program

      function lic(a) result(i)

      implicit none

      double precision :: a

      integer (kind = 2) :: i

      i = int(1000 * log10(a), 2) + 16384

      return

      end function

      function ic(a) result(i)

      implicit none

      double precision :: a

      integer (kind = 2) :: i

      i = int(1000 * a, 2) + 16384

      return

      end function

      function idx(lambda) result(n)

      implicit none

      double precision :: lambda, lambda0, R

      integer (kind = 4) :: n, n0

      lambda0 = 8.97666d0

      R = 500000.0d0

      n0 = int(log10(lambda0) / log10(1.0d0 + 1.0d0 / R), 4)

      n = int(log10(lambda) / log10(1.0d0 + 1.0d0 / R), 4) + 1 - n0

      return

      end function
